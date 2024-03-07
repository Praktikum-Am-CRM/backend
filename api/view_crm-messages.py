from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from crm_messages.models import MessagePool
from crm_messages.serializers import MessagePoolSerializer


class PoolMessageCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = MessagePoolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PoolMessageDeleteAPIView(APIView):
    def delete(self, request, poll_message_id, *args, **kwargs):
        try:
            message = MessagePool.objects.get(id=poll_message_id)
        except MessagePool.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        message.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class BotMessageCreateAPIView(APIView):
#     def post(self, request, *args, **kwargs):
#         serializer = BotMessageSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         return Response(
# serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BotMessageReactionAPIView(APIView):
    def patch(self, request, *args, **kwargs):
        # Your logic for updating bot message reaction
        return Response(status=status.HTTP_204_NO_CONTENT)
