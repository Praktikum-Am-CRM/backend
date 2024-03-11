from django.contrib import admin

from crm_messages.models import (
    BotMessages,
    Message,
    MessagePool,
    MessageStatus,
    MessageType,
)


@admin.register(BotMessages)
class BotMessagesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'ambassador',
        'manager',
        'from_bot',
        'message',
        'sign_ai',
        'message_telegram_id',
        'reaction',
    )


@admin.register(MessageType)
class MessageTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name', 'available')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'message_text', 'media_link', 'message_type', 'date')


@admin.register(MessagePool)
class MessagePoolAdmin(admin.ModelAdmin):
    list_display = ('id', 'message', 'message_status', 'send_date')


@admin.register(MessageStatus)
class MessageStatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'status_name', 'available')
