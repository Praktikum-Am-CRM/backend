from django.utils import timezone
from rest_framework import serializers

from ambassador.models import Ambassador
from ambassador.serializers import AmbassadorShortSerializer
from users.serializer import ManagerSerializer

from .models import (
    BotMessages,
    Message,
    MessagePool,
    MessageStatus,
    MessageType,
)


class MessageTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageType
        fields = ['id', 'type_name', 'available']


class MessageSerializer(serializers.ModelSerializer):
    message_type = MessageTypeSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ['id', 'message_text', 'media_link', 'date', 'message_type']


class MessageStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageStatus
        fields = ['id', 'status_name', 'available']


class MessagePoolSerializer(serializers.ModelSerializer):
    message = MessageSerializer()
    message_status = MessageStatusSerializer()

    class Meta:
        model = MessagePool
        fields = ['id', 'message', 'message_status', 'send_date']


class BotMessageSerializer(serializers.ModelSerializer):
    message = MessageSerializer()
    manager = ManagerSerializer()

    class Meta:
        model = BotMessages
        fields = [
            'id',
            'message',
            'from_bot',
            'manager',
            'sign_ai',
            'message_telegram_id',
            'reaction',
        ]


class BotMessageListSerializer(serializers.ModelSerializer):
    message = MessageSerializer()
    manager = ManagerSerializer()
    ambassador = AmbassadorShortSerializer()

    class Meta:
        model = BotMessages
        fields = [
            'id',
            'message',
            'ambassador',
            'manager',
            'sign_ai',
            'message_telegram_id',
            'reaction',
        ]


class BotMessagesCreateSerializer(serializers.Serializer):
    message_text = serializers.CharField(
        max_length=250,
        required=True,
    )
    ambassadors = serializers.ListSerializer(
        child=serializers.UUIDField(),
        required=False,
    )

    def create(self, validated_data):
        ambassadors_id = validated_data.pop('ambassadors', [])
        message_text = validated_data.pop('message_text', '')

        message = Message.objects.create(
            message_text=message_text, date=timezone.now()
        )
        manager = self.context['request'].user
        ambassadors = (
            Ambassador.objects.filter(id__in=ambassadors_id)
            if (ambassadors_id)
            else Ambassador.objects.all()
        )

        ambassador_messages = []
        for ambassador in ambassadors:
            bot_message = BotMessages(
                message=message,
                from_bot=False,
                manager=manager,
                ambassador=ambassador,
                sign_ai=False,
            )
            ambassador_messages.append(bot_message)
        BotMessages.objects.bulk_create(ambassador_messages)

        # TODO: добавить отправку сообщений в telegram асинхронно

        return message
