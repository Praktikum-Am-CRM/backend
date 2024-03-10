from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.filters import ReportFilter

# from api.paginators import CustomPNPaginator
from reports.models import Report
from reports.serializers import ReportSerializer, ReportUpdateSerializer


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
    # pagination_class = CustomPNPaginator
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ReportFilter

    def get_serializer_class(self):
        if self.action in ('update', 'partial_update'):
            return ReportUpdateSerializer

        return ReportSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}
        serializer = ReportSerializer(instance)
        return Response(serializer.data)

    @action(
        detail=False,
        methods=['get'],
    )
    def unread_reports(self, request):
        unread_reports = Report.objects.filter(report_status=None)
        serializer = ReportSerializer(unread_reports, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
