from django.contrib import admin
from .models import Device

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'device_type', 'status')
    list_filter = ('device_type', 'status', 'date_received')
    search_fields = ('name', 'contact', 'brand', 'model')
    ordering = ('-date_received',)
 