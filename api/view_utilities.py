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
from crm_messages.models import MessagePool, MessageStatus, MessageType
from crm_messages.serializers import (
    MessagePoolSerializer,
    MessageStatusSerializer,
    MessageTypeSerializer,
)
from merches.models import DeliveryStatus
from merches.serializers import DeliveryStatusSerializer
from program.models import Program
from program.serializers import ProgramSerializer
from reports.models import Placement, ReportStatus, ReportType
from reports.serializers import (
    PlacementSerializer,
    ReportStatusSerializer,
    ReportTypeSerializer,
)


@api_view(['GET'])
def get_report_types(request):
    """/api/v1/utility/report_types"""
    report_types = ReportType.objects.all()
    serializer = ReportTypeSerializer(report_types, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_report_statuses(request):
    """/api/v1/utility/report_statuses"""
    report_statuses = ReportStatus.objects.all()
    serializer = ReportStatusSerializer(report_statuses, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_placements(request):
    """/api/v1/utility/placements"""
    placements = Placement.objects.all()
    serializer = PlacementSerializer(placements, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_goals(request):
    """/api/v1/utility/goals"""
    goals = Goal.objects.all()
    serializer = GoalSerializer(goals, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_activities(request):
    """/api/v1/utility/activities"""
    activities = Activity.objects.all()
    serializer = ActivitySerializer(activities, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_ambassador_statuses(request):
    """/api/v1/utility/ambassador_statuses"""
    ambassador_statuses = AmbassadorStatus.objects.all()
    serializer = AmbassadorStatusSerializer(ambassador_statuses, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_achievies(request):
    """/api/v1/utility/achivies"""
    achievies = Achieve.objects.all()
    serializer = AchieveSerializer(achievies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_pool_messages(request):
    """/api/v1/utility/pool_messages"""
    pool_messages = MessagePool.objects.all()
    serializer = MessagePoolSerializer(pool_messages, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_message_statuses(request):
    """/api/v1/utility/message_statuses"""
    message_statuses = MessageStatus.objects.all()
    serializer = MessageStatusSerializer(message_statuses, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_message_types(request):
    """/api/v1/utility/message_types"""
    message_types = MessageType.objects.all()
    serializer = MessageTypeSerializer(message_types, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_delivery_statuses(request):
    """/api/v1/utility/delivery_statuses"""
    delivery_statuses = DeliveryStatus.objects.all()
    serializer = DeliveryStatusSerializer(delivery_statuses, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_programs(request):
    '''/api/v1/utility/programs'''
    programs = Program.objects.all()
    serializer = ProgramSerializer(programs, many=True)
    return Response(serializer.data)
