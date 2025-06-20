<<<<<<< HEAD
from django.contrib import admin
from .models import Device

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'device_type', 'status')
    list_filter = ('device_type', 'status', 'date_received')
    search_fields = ('name', 'contact', 'brand', 'model')
    ordering = ('-date_received',)
=======
from django.contrib import admin
from .models import Device

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'device_type', 'status')
    list_filter = ('device_type', 'status', 'date_received')
    search_fields = ('name', 'contact', 'brand', 'model')
    ordering = ('-date_received',)
 
>>>>>>> c500efc63b6eb4ad91a328a9faa3903e2a7ef3c6
