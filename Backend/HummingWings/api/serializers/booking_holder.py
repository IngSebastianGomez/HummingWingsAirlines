from rest_framework import serializers
from ..models.booking_holder import BookingHolder  

class BookingHolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingHolder
        fields = '__all__'