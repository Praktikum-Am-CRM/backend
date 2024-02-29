from rest_framework.decorators import api_view
from rest_framework.response import Response

from achievements.models import Achieve
from achievements.serializers import AchieveSerializer

from ambassador.models import Activity, AmbassadorStatus, Goal
from ambassador.serializers import (
    ActivitySerializer,
    AmbassadorStatusSerializer,
    GoalSerializer,
)
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


@api_view(['GET'])
def get_goals(request):
    '''/api/v1/utility/goals'''
    report_types = Goal.objects.all()
    serializer = GoalSerializer(report_types, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_activities(request):
    '''/api/v1/utility/activities'''
    report_types = Activity.objects.all()
    serializer = ActivitySerializer(report_types, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_ambassador_statuses(request):
    '''/api/v1/utility/ambassador_statuses'''
    report_types = AmbassadorStatus.objects.all()
    serializer = AmbassadorStatusSerializer(report_types, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_achivies(request):
    '''/api/v1/utility/achivies'''
    report_types = Achieve.objects.all()
    serializer = AchieveSerializer(report_types, many=True)
    return Response(serializer.data)