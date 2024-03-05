from http import HTTPStatus

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ambassador.filters import AmbassadorFilter
from ambassador.models import Ambassador
from ambassador.serializers import AmbassadorSerializer
from crm_messages.models import BotMessages
from crm_messages.serializers import BotMessagesSerializer
from reports.models import Report
from reports.serializers import ReportSerializer
from telegram.models import TelegramBot


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


# def create_ambassador(request):
#     '''Создание Амбассадора.'''
#     serializer = AmbassadorSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=HTTPStatus.OK)
#     return Response(serializer.errors, status=HTTPStatus.BAD_REQUEST)


@api_view(['POST'])
def create_or_update_ambassador(request, telegram_id):
    try:
        ambassador = Ambassador.objects.get(
            telegram_bot__telegram_id=telegram_id
        )
        ambassador.first_name = request.data['first_name']
        ambassador.last_name = request.data['last_name']
        ambassador.email = request.data['email']
        ambassador.save()
        return ambassador
    except Ambassador.DoesNotExist:
        try:
            telegram_bot = TelegramBot.objects.get(telegram_id=telegram_id)
            ambassador = Ambassador.objects.create(
                first_name=request.data['first_name'],
                last_name=request.data['last_name'],
                email=request.data['email'],
                telegram_bot=telegram_bot,
            )
            return ambassador
        except TelegramBot.DoesNotExist:
            # Если не удалось найти соответствующую запись в TelegramBot
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
