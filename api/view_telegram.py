from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

from telegram.serializers import TelegramBotSerializer


class TelegramUserCreateView(mixins.CreateModelMixin, viewsets.ViewSet):
    serializer_class = TelegramBotSerializer

    def get_serializer(self, *args, **kwargs):
        return self.serializer_class(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(status=status.HTTP_204_NO_CONTENT)
