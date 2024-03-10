# from rest_framework import mixins, permissions, status, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from ambassador.models import Ambassador
from ambassador.serializers import (
    AmbassadorBotCreateSerializer,
    AmbassadorSerializer,
    AmbassadorUpdateSerializer,
)
from crm_messages.models import BotMessages
from crm_messages.serializers import BotMessageSerializer
from merches.models import AmbassadorRequest
from merches.serializers import AmbassadorRequestSerializer
from reports.models import Report
from reports.serializers import ReportForAmbassadorSerializer

from .filters import AmbassadorFilter
from .paginators import CustomPNPaginator


class AmbassadorViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Ambassador.objects.all()
    serializer_class = AmbassadorSerializer
    permission_classes = (permissions.IsAuthenticated,)
    pagination_class = CustomPNPaginator
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AmbassadorFilter

    def get_serializer_class(self):
        if self.action == 'create':
            return AmbassadorBotCreateSerializer

        if self.action in ['update', 'partial_update']:
            return AmbassadorUpdateSerializer

        return AmbassadorSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}
        serializer = AmbassadorSerializer(instance)
        return Response(serializer.data)

    @action(
        detail=True,
        methods=['get'],
    )
    def reports(self, request, pk):
        ambassador = get_object_or_404(Ambassador, id=pk)

        reports = Report.objects.filter(ambassador=ambassador)
        serializer = ReportForAmbassadorSerializer(reports, many=True)

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

    @action(detail=True, methods=['get'])
    def messages(self, request, pk):
        ambassador = get_object_or_404(Ambassador, id=pk)
        messages = BotMessages.objects.filter(ambassador=ambassador)
        serializer = BotMessageSerializer(messages, many=True)
        return Response(serializer.data)
