from rest_framework import serializers
from .models import Category, Product, Order, OrderItem, Customer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    class Meta:
        model = OrderItem
        fields = ['id','product','quantity','get_total']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, source='orderitem_set', read_only=True)
    class Meta:
        model = Order
        fields = ['id','customer','complete','transaction_id','items','get_cart_price']
