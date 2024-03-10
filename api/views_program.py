from rest_framework import mixins, permissions, viewsets

from ambassador.serializers import AmbassadorProgramSerializer
from program.models import Program


class AmbassadorProgramViewsList(
    mixins.ListModelMixin, viewsets.GenericViewSet
):
    queryset = Program.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = AmbassadorProgramSerializer
