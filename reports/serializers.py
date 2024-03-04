import base64

from django.core.files.base import ContentFile
from rest_framework import serializers

from .models import Placement, ReportStatus, ReportType


class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            format, imgstr = data.split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)

        return super().to_internal_value(data)


class ReportTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportType
        fields = ['id', 'type_name', 'available']


class ReportStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportStatus
        fields = ['id', 'status_name', 'available']


class PlacementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Placement
        fields = ['id', 'site', 'available']
