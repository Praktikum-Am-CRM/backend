from rest_framework import status, viewsets
from rest_framework.response import Response

from ambassador.models import Ambassador
from crm_messages.models import BotMessages, Message


class SendMessageToTelegramViewSet(viewsets.ViewSet):
    def create(self, request):
        message_text = request.data.get('message_text')
        ambassadors = request.data.get('ambassadors', [])
        message = Message.objects.create(message_text=message_text)
        if ambassadors:
            ambassadors_from_db = Ambassador.objects.filter(id__in=ambassadors)
        else:
            ambassadors_from_db = Ambassador.objects.all()
        messages_for_send = []
        for ambassador in ambassadors_from_db:
            bot_message = BotMessages(
                message=message,
                manager=request.user,
                from_bot=False,
                ambassador=ambassador,
                sign_ai=False,
            )
            messages_for_send.append(bot_message)
        BotMessages.objects.bulk_create(messages_for_send)
        # TODO: добавить отправку сообщений в telegram асинхронно
        return Response(
            {'detail': 'Messages saved successfully'},
            status=status.HTTP_201_CREATED,
        )
