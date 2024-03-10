from rest_framework import mixins, permissions, viewsets

from merches.models import MerchRequest
from merches.serializers import MerchRequestSerializer


class MerchesViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = MerchRequestSerializer
    queryset = MerchRequest.objects.all()
