# listings/serializers.py

from rest_framework import serializers
from .models import Listing, Booking

class ListingSerializer(serializers.ModelSerializer):
    """
    Serializer for the Listing model.
    """
    class Meta:
        model = Listing
        fields = [
            'id', 
            'host', 
            'title', 
            'description', 
            'address', 
            'price_per_night', 
            'bedrooms', 
            'bathrooms', 
            'created_at'
        ]
        read_only_fields = ['host', 'created_at']

class BookingSerializer(serializers.ModelSerializer):
    """
    Serializer for the Booking model.
    """
    class Meta:
        model = Booking
        fields = [
            'id', 
            'listing', 
            'guest', 
            'check_in_date', 
            'check_out_date', 
            'status', 
            'created_at'
        ]
        read_only_fields = ['guest', 'created_at']