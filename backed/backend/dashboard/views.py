from django.shortcuts import render
from app.models import *

def home(request):
    context = {
        "users_count": Customer.objects.count(),
        "products_count": Product.objects.count(),
        "categories_count": Category.objects.count(),
        "orders_count": Order.objects.count(),
    }
    return render(request, 'dashboard/home.html', context)

def users(request):
    users = Customer.objects.all()
    return render(request, 'dashboard/users.html', {'users': users})

def products(request):
    products = Product.objects.all()
    return render(request, 'dashboard/products.html', {'products': products})

def categories(request):
    categories = Category.objects.all()
    return render(request, 'dashboard/categories.html', {'categories': categories})

def orders(request):
    orders = Order.objects.all()
    
    completed_orders_count = orders.filter(complete=True).count()
    pending_orders_count = orders.filter(complete=False).count()
    total_revenue = sum(order.get_cart_price for order in orders if order.complete)
    
    context = {
        'orders': orders,
        'orders_count': orders.count(),
        'completed_orders_count': completed_orders_count,
        'pending_orders_count': pending_orders_count,
        'total_revenue': total_revenue,
    }
    return render(request, 'dashboard/orders.html', context)