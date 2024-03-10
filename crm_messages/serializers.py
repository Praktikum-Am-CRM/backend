from rest_framework import serializers

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
