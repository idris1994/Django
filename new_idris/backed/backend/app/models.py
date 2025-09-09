from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=56)
    discout = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=256)
    price = models.BigIntegerField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    discount = models.IntegerField(default=0)
    featured_image = models.ImageField(blank=True, null=True) 
    # additional_images
    description = models.TextField()
    digital = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.name} | {self.category} - Price: {self.price}/-"
    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateField(auto_now=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.id} - {self.customer.name}" 
    
    @property
    def get_cart_items(self):
        items = self.orderitem_set.all()
        total = sum([item.quantity for item in items])
        return total
    
    @property
    def get_cart_price(self):
        total = sum([item.get_total for item in self.orderitem_set.all()])
        return total
    
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField()
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.order.pk} | {self.product.name} ({self.quantity})"
    
    @property
    def get_total(self):
        price = self.quantity * self.product.price
        return price
        

class Checkout(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    address = models.TextField(max_length=256)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"