from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_booking_confirmation_email(customer_email, booking_details):
    subject = "Booking Confirmation - ALX Travel App"
    message = f"Thank you for your booking!\n\nDetails: {booking_details}"
    recipient_list = [customer_email]
    
    send_mail(subject, message, None, recipient_list)