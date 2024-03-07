from rest_framework import serializers

from ambassador.serializers import AmbassadorShortSerializer
from users.serializer import ManagerSerializer

from .models import (
    AmbassadorRequest,
    DeliveryAddress,
    DeliveryStatus,
    Merch,
    MerchRequest,
)


class DeliveryStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryStatus
        fields = ['id', 'status_name', 'available']


class DeliveryAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryAddress
        fields = '__all__'


class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merch
        fields = '__all__'


class MerchRequestSerializer(serializers.ModelSerializer):
    merch = MerchSerializer()
    manager = ManagerSerializer()
    request_status = DeliveryStatusSerializer()
    delivery_address = DeliveryAddressSerializer()
    ambassadors = serializers.SerializerMethodField()

    class Meta:
        model = MerchRequest
        fields = '__all__'

    def get_ambassadors(self, obj):
        ambassador_request = AmbassadorRequest.objects.filter(
            merch_request=obj
        )
        if ambassador_request:
            ambassador_serializer = AmbassadorShortSerializer(
                ambassador_request[0].ambassador
            )
            return ambassador_serializer.data
        return {}


class AmbassadorRequestSerializer(serializers.ModelSerializer):
    request_id = serializers.UUIDField(source='merch_request.id')
    request_merch = serializers.SerializerMethodField()
    request_status = serializers.SerializerMethodField()
    request_delivery_address = serializers.SerializerMethodField()

    class Meta:
        model = AmbassadorRequest
        fields = [
            'id',
            'request_id',
            'request_merch',
            'assignment_date',
            'request_status',
            'request_delivery_address',
        ]

    def get_request_merch(self, obj):
        merch_ser = MerchSerializer(obj.merch_request.merch)

        return merch_ser.data

    def get_request_status(self, obj):
        request_status_ser = DeliveryStatusSerializer(
            obj.merch_request.request_status
        )

        return request_status_ser.data

    def get_request_delivery_address(self, obj):
        request_delivery_address_ser = DeliveryAddressSerializer(
            obj.merch_request.delivery_address
        )

        return request_delivery_address_ser.data
