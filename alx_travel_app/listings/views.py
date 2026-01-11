from rest_framework import viewsets
from .models import Listing, Booking
from .serializers import ListingSerializer, BookingSerializer
from .tasks import send_booking_confirmation_email

class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

    def perform_create(self, serializer):
        serializer.save(host=self.request.user)

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def perform_create(self, serializer):
        # 1. Save the booking instance
        booking = serializer.save(guest=self.request.user)
        
        # 2. Extract details for the email
        guest_email = booking.guest.email
        listing_name = booking.listing.property_name  # Adjust field name based on your Model
        booking_details = f"Property: {listing_name}, Check-in: {booking.start_date}"

        # 3. Trigger the Celery task asynchronously
        send_booking_confirmation_email.delay(guest_email, booking_details)