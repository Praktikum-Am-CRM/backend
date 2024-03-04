from http import HTTPStatus

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ambassador.filters import AmbassadorFilter
from ambassador.models import Ambassador
from crm_messages.models import BotMessages
from crm_messages.serializers import BotMessagesSerializer
from reports.models import Report
from reports.serializers import ReportSerializer

from .serializers import AmbassadorSerializer


class AmbassadorViewList(generics.ListAPIView):
    queryset = Ambassador.objects.all()
    serializer_class = AmbassadorSerializer
    filter_backends = (
        DjangoFilterBackend,
        AmbassadorFilter,
        filters.SearchFilter,
    )
    search_fields = [
        'first_name',
        'last_name',
        'middle_name',
        'email',
        # 'program',
    ]
    ordering_fields = [
        'first_name',
        'last_name',
        'middle_name',
        'receipt_date',
        # 'program',
        'gender',
        'status',
    ]


@api_view(['POST'])
def create_ambassador(request):
    '''Создание Амбассадора.'''
    serializer = AmbassadorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=HTTPStatus.OK)
    return Response(serializer.errors, status=HTTPStatus.BAD_REQUEST)


@api_view(['PATCH'])
def update_ambassador(request, ambassador_id):
    '''Обновление данных Амбассадора по id.'''
    try:
        ambassador = Ambassador.objects.get(id=ambassador_id)
        serializer = AmbassadorSerializer(
            ambassador, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTPStatus.OK)
        return Response(serializer.errors, status=HTTPStatus.BAD_REQUEST)
    except Ambassador.DoesNotExist:
        return Response(status=HTTPStatus.NOT_FOUND)


@api_view(['GET'])
def get_ambassador_reports(request, ambassador_id):
    '''Получение отчетов Амбассадора.'''
    reports = Report.objects.filter(ambassador=ambassador_id)
    serializer = ReportSerializer(reports, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_ambassador_messages(request, ambassador_id):
    '''Получение сообщений Амбассадора.'''
    messages = BotMessages.objects.filter(ambassador=ambassador_id)
    serializer = BotMessagesSerializer(messages, many=True)
    return Response(serializer.data)
