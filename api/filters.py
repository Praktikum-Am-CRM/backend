import django_filters

from ambassador.models import Ambassador, AmbassadorStatus


class AmbassadorFilter(django_filters.FilterSet):
    status = django_filters.ModelMultipleChoiceFilter(
        field_name='status__id',
        to_field_name='id',
        queryset=AmbassadorStatus.objects.all(),
    )

    class Meta:
        model = Ambassador
        fields = ['status']
