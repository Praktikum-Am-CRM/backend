from django.utils import timezone
from rest_framework import serializers

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

    class Meta:
        model = TelegramBot
        fields = ['telegram_id', 'nickname', 'registration_date']
