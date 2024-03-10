import base64

from django.core.files.base import ContentFile
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from ambassador.serializers import AmbassadorShortSerializer

from .models import Placement, Report, ReportStatus, ReportType


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


class ReportForAmbassadorSerializer(serializers.ModelSerializer):
    placement = PlacementSerializer()
    report_status = ReportStatusSerializer()
    report_type = ReportTypeSerializer()

    class Meta:
        model = Report
        fields = [
            'id',
            'report_date',
            'content_link',
            'screen',
            'placement',
            'report_status',
            'sign_junior',
            'grade',
            'report_type',
        ]


class ReportListSerializer(serializers.ModelSerializer):
    placement = PlacementSerializer()
    report_status = ReportStatusSerializer()
    report_type = ReportTypeSerializer()
    ambassador = AmbassadorShortSerializer()

    class Meta:
        model = Report
        fields = [
            'id',
            'ambassador',
            'report_date',
            'content_link',
            'screen',
            'placement',
            'report_status',
            'sign_junior',
            'grade',
            'report_type',
        ]


class ReportUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = [
            'report_status',
            'grade',
        ]

    def validate_grade(self, value):
        if value < 1 or value > 10:
            raise ValidationError('Оценка должна быть в диапазоне от 1 до 10')
        return value
