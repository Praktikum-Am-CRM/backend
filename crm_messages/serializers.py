from rest_framework import serializers

from crm_messages.admin import BotMessagesAdmin
from users.serializers import ManagerSerializer

from .models import Message, MessagePool, MessageStatus, MessageType


class MessageSerializer(serializers.ModelSerializer):
    message_type = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Message
        fields = ['id', 'message_text', 'media_link', 'date', 'message_type']


class MessageTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageType
        fields = ['id', 'type_name', 'available']


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



class BotMessagesSerializer(serializers.ModelSerializer):
    message_type = MessageTypeSerializer()
    manager = ManagerSerializer()

    class Meta:
        model = BotMessagesAdmin
        fields = [
            'id',
            'message',
            'from_bot',
            'manager',
            'sign_ai',
            'message_telegram_id',
            'reaction',
        ]

