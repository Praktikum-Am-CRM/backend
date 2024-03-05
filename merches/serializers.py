from rest_framework import serializers

from .models import DeliveryStatus


class DeliveryStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryStatus
        fields = ['id', 'status_name', 'available']
