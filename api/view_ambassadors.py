# from rest_framework import mixins, permissions, status, viewsets
from rest_framework import mixins, viewsets

from ambassador.models import Ambassador
from ambassador.serializers import AmbassadorSerializer

from .paginators import CustomPNPaginator

# from rest_framework.decorators import action
# from rest_framework.response import Response


class AmbassadorViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Ambassador.objects.all()
    serializer_class = AmbassadorSerializer
    pagination_class = CustomPNPaginator
