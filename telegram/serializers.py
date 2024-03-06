from rest_framework import serializers

from .models import TelegramBot


class TelegramBotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramBot
        fields = ["telegram_id", "nickname", "registration_date", "active"]
