import django_filters

from django_filters.rest_framework import FilterSet
from django_filters.rest_framework import CharFilter

from .models import GeneralInfo


class GenInfoFilter(FilterSet):
    """自定义过滤器-一般信息的过滤"""

    name = CharFilter(field_name="name", lookup_expr='icontains')
    nation = CharFilter(field_name="nation", lookup_expr='contains')

    class Meta:
        model = GeneralInfo
        fields = ['name', 'nation']
