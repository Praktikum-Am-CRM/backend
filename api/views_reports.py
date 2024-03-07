from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from reports.models import Report
from reports.serializers import ReportSerializer


class ReportViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [IsAuthenticated]
