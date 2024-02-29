from rest_framework.decorators import api_view
from rest_framework.response import Response

from reports.models import Placement, ReportStatus, ReportType
from reports.serializers import (
    PlacementSerializer,
    ReportStatusSerializer,
    ReportTypeSerializer,
)


@api_view(['GET'])
def get_report_types(request):
    '''/api/v1/utility/report_types'''
    report_types = ReportType.objects.all()
    serializer = ReportTypeSerializer(report_types, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_report_statuses(request):
    '''/api/v1/utility/report_statuses'''
    report_types = ReportStatus.objects.all()
    serializer = ReportStatusSerializer(report_types, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_placements(request):
    '''/api/v1/utility/placements'''
    report_types = Placement.objects.all()
    serializer = PlacementSerializer(report_types, many=True)
    return Response(serializer.data)