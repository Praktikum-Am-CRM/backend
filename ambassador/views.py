from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from ambassador.models import Ambassador

from .serializers import AmbassadorSerialisers


class AmbassadorViewList(generics.ListAPIView):
    queryset = Ambassador.objects.all()
    serializer_class = AmbassadorSerialisers
    filter_backends = (DjangoFilterBackend,)
