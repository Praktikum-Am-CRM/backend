from rest_framework import mixins, permissions, status, viewsets
from rest_framework.response import Response

from crm_messages.models import BotMessages
from crm_messages.serializers import (
    BotMessageListSerializer,
    BotMessagesCreateSerializer,
)


class BotMessagesViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = BotMessages.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == 'create':
            return BotMessagesCreateSerializer

        return BotMessageListSerializer

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return Response(status=status.HTTP_201_CREATED)
