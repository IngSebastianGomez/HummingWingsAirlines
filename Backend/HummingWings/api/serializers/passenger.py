from rest_framework import serializers
from ..models.passenger import Passenger

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'
