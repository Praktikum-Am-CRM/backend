import django_filters
from django.db.models import Q

from ambassador.models import Ambassador, AmbassadorStatus
from reports.models import Report, ReportStatus


class AmbassadorFilter(django_filters.FilterSet):
    status = django_filters.ModelMultipleChoiceFilter(
        field_name='status__id',
        to_field_name='id',
        queryset=AmbassadorStatus.objects.all(),
    )

    search = django_filters.CharFilter(method='search_filter')

    class Meta:
        model = Ambassador
        fields = ['status']

    def search_filter(self, queryset, name, value):
        if value:
            return queryset.filter(
                Q(first_name__istartswith=value)
                | Q(last_name__istartswith=value)
            )
        return queryset


class ReportFilter(django_filters.FilterSet):
    status = django_filters.ModelMultipleChoiceFilter(
        field_name='report_status__id',
        to_field_name='id',
        queryset=ReportStatus.objects.all(),
    )

    class Meta:
        model = Report
        fields = ['status']
