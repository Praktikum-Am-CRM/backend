from django_filters import rest_framework as filters

from ambassador.models import Ambassador


class AmbassadorFilter(filters.FilterSet):
    class Meta:
        model = Ambassador
        fields = {
            'status': ['exact'],
            'gender': ['exact'],
            # 'program': ['exact'], нет связи с программой в модели
        }
