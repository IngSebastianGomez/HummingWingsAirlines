from rest_framework import serializers
from ..models.payment_log import PaymentLog

class PaymentLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentLog
        fields = '__all__'
