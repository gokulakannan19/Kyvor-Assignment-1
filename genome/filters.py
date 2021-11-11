import django_filters
from django_filters import CharFilter
from .models import Gene


class GeneFilter(django_filters.FilterSet):
    variant = CharFilter(field_name='variant', lookup_expr="icontains")

    class Meta:
        model = Gene
        fields = ['variant']
