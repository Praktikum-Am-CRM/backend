from django.contrib import admin

from .models import TelegramBot


@admin.register(TelegramBot)
class TelegramBotAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'telegram_id',
        'nickname',
        'registration_date',
        'active',
    )
