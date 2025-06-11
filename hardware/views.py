# hardware/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Device
from .forms import DeviceForm
from .filters import DeviceFilter  # Import the filter class

def device_list(request):
    devices = Device.objects.all()
    device_filter = DeviceFilter(request.GET, queryset=devices)  # Apply the filter
    devices = device_filter.qs  # Get the filtered queryset

    return render(request, 'hardware/device_list.html', {
        'devices': devices,
        'device_filter': device_filter,  # Pass the filter to the template
    })

# View details of a specific device
def device_detail(request, pk):
    device = get_object_or_404(Device, pk=pk)
    return render(request, 'hardware/device_detail.html', {'device': device})

# Create a new device
def device_create(request):
    if request.method == 'POST':
        form = DeviceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hardware:device_list')
    else:
        form = DeviceForm()
    return render(request, 'hardware/device_form.html', {'form': form})

# Update an existing device
def device_update(request, pk):
    device = get_object_or_404(Device, pk=pk)
    if request.method == 'POST':
        form = DeviceForm(request.POST, instance=device)
        if form.is_valid():
            form.save()
            return redirect('hardware:device_list')
    else:
        form = DeviceForm(instance=device)
    return render(request, 'hardware/device_form.html', {'form': form})

# Delete a device
def device_delete(request, pk):
    device = get_object_or_404(Device, pk=pk)
    if request.method == 'POST':
        device.delete()
        return redirect('hardware:device_list')
    return render(request, 'hardware/device_confirm_delete.html', {'device': device})