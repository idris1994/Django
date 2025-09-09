from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='dashboard_home'),
    path('users', views.users, name='dashboard_users'),
    path('products', views.products, name='dashboard_products'),
    path('categories', views.categories, name='dashboard_categories'),
    path('orders', views.orders, name='dashboard_orders'),
]
