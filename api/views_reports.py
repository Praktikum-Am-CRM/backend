from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from reports.models import Report
from reports.serializers import ReportSerializer


class ReportViewSet(
    mixins.ListModelMixin,
    # mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    # mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [IsAuthenticated]

    @action(
        detail=True,
        methods=['get'],
    )
    def unread_reports(self, request):
        unread_reports = Report.objects.filter(report_status=None)
        serializer = ReportSerializer(unread_reports, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
