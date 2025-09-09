from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('shop/', views.shop, name='shop'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('checkout-page/', views.checkout_page, name='checkout_page'),
    path('product/', views.product, name='product'),
    path('payment-done/', views.payment_done, name='payment_done'),
]