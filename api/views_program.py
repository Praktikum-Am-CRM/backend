from rest_framework import mixins, permissions, viewsets

from program.models import Program
from program.serializers import ProgramSerializer


class AmbassadorProgramViewsList(
    mixins.ListModelMixin, viewsets.GenericViewSet
):
    queryset = Program.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ProgramSerializer
