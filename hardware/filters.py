# filters.py
import django_filters
from .models import Device

class DeviceFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', label='Name')
    brand = django_filters.CharFilter(lookup_expr='icontains', label='Brand')
    model = django_filters.CharFilter(lookup_expr='icontains', label='Model')

    class Meta:
        model = Device
        fields = ['name', 'brand', 'model']