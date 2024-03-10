from django.utils import timezone
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from backend.constants import MAX_NAME_LENGTH

from .models import TelegramBot


class TelegramBotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramBot
        fields = [
            'id',
            'telegram_id',
            'nickname',
            'registration_date',
            'active',
        ]


class TelegramBotCreateSerializer(serializers.ModelSerializer):
    registration_date = serializers.DateTimeField(default=timezone.now)
    telegram_id = serializers.CharField(
        max_length=100,
        required=True,
        validators=[UniqueValidator(queryset=TelegramBot.objects.all())],
    )
    nickname = serializers.CharField(max_length=MAX_NAME_LENGTH)

    class Meta:
        model = TelegramBot
        fields = ['telegram_id', 'nickname', 'registration_date']
