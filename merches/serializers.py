from rest_framework import serializers

from .models import AmbassadorRequest, DeliveryStatus, Merch, MerchRequest


class DeliveryStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryStatus
        fields = ['id', 'status_name', 'available']


class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merch
        fields = '__all__'


class MerchRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MerchRequest
        fields = '__all__'


class AmbassadorRequestSerializer(serializers.ModelSerializer):
    merch_request_id = serializers.UUIDField(source='merch_request.id')
    merch_request_merch = serializers.SerializerMethodField()

    class Meta:
        model = AmbassadorRequest
        fields = [
            'id',
            'merch_request_id',
            'merch_request_merch',
            'assignment_date',
        ]

    def get_merch_request_merch(self, obj):
        merch_ser = MerchSerializer(obj.merch_request.merch)

        return merch_ser.data
