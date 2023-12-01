from rest_framework import serializers

from ..serializers.passenger import PassengerSerializer
from ..serializers.payment_log import PaymentLogSerializer

from ..models.booking_holder import BookingHolder
from ..models.passenger import Passenger
from ..models.payment_log import PaymentLog

class BookingHolderSerializer(serializers.ModelSerializer):
    
    payment_logs = serializers.SerializerMethodField("get_payment_logs")
    passengers = serializers.SerializerMethodField("get_passengers")
    
    class Meta:
        model = BookingHolder
        fields = '__all__'

    def get_payment_logs(self, obj):
        """ Get all payment logs related to this booking holder """
        payments = PaymentLog.objects.filter(booking_holder=obj).all()
        return PaymentLogSerializer(payments, many=True).data

    def get_passengers(self, obj):
        """ Get all passengers related to this booking holder """
        passengers = Passenger.objects.filter(booking_holder=obj).all()
        return PassengerSerializer(passengers, many=True).data
