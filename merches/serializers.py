from rest_framework import serializers

from .models import DeleviryStatus


class DeliveryStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeleviryStatus
        fields = ['id', 'status_name', 'available']
