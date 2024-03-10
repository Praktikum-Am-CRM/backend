from rest_framework import mixins, permissions, viewsets

from ambassador.models import AmbassadorStatus
from ambassador.serializers import AmbassadorStatSerializer


class AmbassadorStatusViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = AmbassadorStatus.objects.all()
    serializer_class = AmbassadorStatSerializer
    permission_classes = (permissions.IsAuthenticated,)
