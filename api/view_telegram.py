from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from telegram.serializers import TelegramBotSerializer


class TelegramUserCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = TelegramBotSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
