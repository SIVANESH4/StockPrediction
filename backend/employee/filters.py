import django_filters
from rest_framework.response import Response
from .models import Employee_table

class EmployeeFilters(django_filters.FilterSet):
    emp_designation = django_filters.CharFilter(field_name='emp_designation', lookup_expr='iexact'),
    emp_name = django_filters.CharFilter(field_name='emp_name', lookup_expr='icontains'),
    id_min = django_filters.CharFilter(method='filter_by_id', label='From'),
    id_max = django_filters.CharFilter(method='filter_by_id', label='To')

    def filter_by_id(self, queryset, name, value):
        if name == 'id_min':
            return queryset.filter(emp_id__gte = value)
        elif name == 'id_max':
            return queryset.filter(emp_id__lte = value)
        return queryset
    
    class Meta:
        model = Employee_table
        fields = ['emp_designation', 'emp_name', 'emp_id']

    