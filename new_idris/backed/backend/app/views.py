from django.shortcuts import render, redirect
from .models import *

def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {'categories': categories, 'products': products}
    return render(request, 'index-1.html', context)

def shop(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {'categories': categories, 'products': products}
    return render(request, 'shop.html', context)

def cart(request):
    categories = Category.objects.all()
    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(customer=request.user.customer)
        orderitems = order.orderitem_set.all()
    else:
        order = None
        orderitems = []
    context = {'categories': categories, 'order': order, 'orderitems': orderitems}
    return render(request, 'cart.html', context)

def checkout_page(request):
    categories = Category.objects.all()
    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(customer=request.user.customer)
        orderitems = order.orderitem_set.all()
    else:
        order = None
        orderitems = []
    context = {'categories': categories, 'order': order, 'orderitems': orderitems}
    return render(request, 'checkout.html', context)


def checkout_view(request):
    categories = Category.objects.all()
    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(customer=request.user.customer)
        orderitems = order.orderitem_set.all()
    else:
        order = None
        orderitems = []

    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        street_address1 = request.POST.get("street_address1")
        street_address2 = request.POST.get("street_address2")
        address = f"{street_address1} {street_address2}".strip()

        Checkout.objects.create(
            first_name=first_name,
            last_name=last_name,
            address=address
        )

        return redirect("payment_done")
    
    context = {
        'categories': categories,
        'order': order,
        'orderitems': orderitems
    }

    return render(request, "checkout.html", context)


def payment_done(request):
    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(customer=request.user.customer)
    else:
        order = None
    return render(request, 'payment_success.html', {'order': order})


def product(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'product.html', context)



