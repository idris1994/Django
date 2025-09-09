from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product, Category, Order, OrderItem
from .serializers import ProductSerializer, CategorySerializer, OrderSerializer
from rest_framework.permissions import IsAuthenticated
import time

class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        # if Product has owner field: compare owner.user == request.user
        owner = getattr(obj, 'owner', None)
        if owner is not None:
            try:
                return owner.user == request.user
            except Exception:
                return False
        return False

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrAdmin]

    def perform_create(self, serializer):
        # set owner if you have such field; otherwise just save
        serializer.save()

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CartAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        customer = request.user.customer
        order, _ = Order.objects.get_or_create(customer=customer, complete=False)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def post(self, request):
        # expected: {"product_id":1,"action":"add","quantity":1}
        product_id = request.data.get('product_id')
        action = request.data.get('action')
        quantity = int(request.data.get('quantity', 1))
        customer = request.user.customer
        order, _ = Order.objects.get_or_create(customer=customer, complete=False)
        product = Product.objects.get(pk=product_id)
        order_item, _ = OrderItem.objects.get_or_create(order=order, product=product)
        if action == 'add':
            order_item.quantity += quantity
            order_item.save()
        elif action == 'remove':
            order_item.quantity -= quantity
            if order_item.quantity <= 0:
                order_item.delete()
            else:
                order_item.save()
        elif action == 'set':
            if quantity <= 0:
                order_item.delete()
            else:
                order_item.quantity = quantity
                order_item.save()
        return Response({'ok': True}, status=status.HTTP_200_OK)

class PlaceOrderAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        # Simple mock payment: mark order complete and set transaction id
        customer = request.user.customer
        order = Order.objects.filter(customer=customer, complete=False).first()
        if not order:
            return Response({'detail':'No open order'}, status=400)
        order.complete = True
        order.transaction_id = f"TX-{order.pk}-{int(time.time())}"
        order.save()

        # trigger celery task (if configured)
        try:
            from .tasks import send_order_confirmation_email
            send_order_confirmation_email.delay(order.id)
        except Exception:
            pass

        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class OrderViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Order.objects.all()
        if hasattr(user, 'customer'):
            return Order.objects.filter(customer=user.customer)
        return Order.objects.none()
