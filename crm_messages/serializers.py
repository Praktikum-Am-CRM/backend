from rest_framework import serializers

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
