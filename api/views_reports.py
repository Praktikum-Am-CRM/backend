from django.shortcuts import get_object_or_404
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from reports.models import Report, ReportStatus
from reports.serializers import ReportSerializer, ReportStatusSerializer


class ReportViewSet(
    mixins.ListModelMixin,
    # mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [IsAuthenticated]

    @action(
        detail=False,
        methods=['get'],
    )
    def unread_reports(self, request):
        unread_reports = Report.objects.filter(report_status=None)
        serializer = ReportSerializer(unread_reports, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(
        detail=True,
        methods=['patch'],
    )
    def update_report_status(self, request, pk):
        report = get_object_or_404(Report, id=pk)

        report_status = ReportStatus.objects.filter(reports=report)
        serializer = ReportStatusSerializer(
            report_status, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
