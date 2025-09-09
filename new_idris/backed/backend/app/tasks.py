from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_order_confirmation(email, order_id):
    send_mail(
        "Order Confirmation",
        f"Your order {order_id} has been placed successfully!",
        "no-reply@myshop.com",
        [email],
        fail_silently=False,
    )
