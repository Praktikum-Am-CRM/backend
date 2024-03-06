# from rest_framework import mixins, permissions, status, viewsets
from rest_framework import mixins, permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ambassador.models import Ambassador
from ambassador.serializers import AmbassadorSerializer
from reports.models import Report
from reports.serializers import ReportSerializer

from .paginators import CustomPNPaginator


class AmbassadorViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    queryset = Ambassador.objects.all()
    serializer_class = AmbassadorSerializer
    permission_classes = (permissions.IsAuthenticated,)
    pagination_class = CustomPNPaginator

    @action(
        detail=True,
        methods=['get'],
    )
    def reports(self, request, pk):
        ambassador = Ambassador.objects.filter(id=pk)
        if not ambassador:
            return Response(status=status.HTTP_404_NOT_FOUND)

        reports = Report.objects.filter(ambassador=ambassador[0])
        serializer = ReportSerializer(reports, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
