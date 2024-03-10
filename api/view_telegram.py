from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

from telegram.serializers import TelegramBotCreateSerializer


class TelegramUserCreateView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = TelegramBotCreateSerializer

    def perform_create(self, serializer):
        serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(status=status.HTTP_204_NO_CONTENT)
