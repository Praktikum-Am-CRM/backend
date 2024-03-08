# from rest_framework import mixins, permissions, status, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from ambassador.models import Ambassador
from ambassador.serializers import AmbassadorSerializer
from merches.models import AmbassadorRequest
from merches.serializers import AmbassadorRequestSerializer
from reports.models import Report
from reports.serializers import ReportSerializer

from .filters import AmbassadorFilter
from .paginators import CustomPNPaginator


class AmbassadorViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    queryset = Ambassador.objects.all()
    serializer_class = AmbassadorSerializer
    permission_classes = (permissions.IsAuthenticated,)
    pagination_class = CustomPNPaginator
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AmbassadorFilter

    @action(
        detail=True,
        methods=['get'],
    )
    def reports(self, request, pk):
        ambassador = get_object_or_404(Ambassador, id=pk)

        reports = Report.objects.filter(ambassador=ambassador)
        serializer = ReportSerializer(reports, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'])
    def merches(self, request, pk):
        ambassador = get_object_or_404(Ambassador, id=pk)

        ambassador_requests = AmbassadorRequest.objects.filter(
            ambassador=ambassador
        )
        ambassador_requests_serializer = AmbassadorRequestSerializer(
            ambassador_requests, many=True
        )

        return Response(
            ambassador_requests_serializer.data, status=status.HTTP_200_OK
        )
