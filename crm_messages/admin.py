from django.contrib import admin  # noqa

from crm_messages.models import (
    BotMessages,
    Message,
    MessagePool,
    MessageStatus,
    MessageType,
)

admin.site.register(BotMessages)
admin.site.register(MessageType)
admin.site.register(Message)
admin.site.register(MessagePool)
admin.site.register(MessageStatus)
