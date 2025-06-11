# forms.py
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column
from .models import Device

class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = [
            'name', 'contact', 'device_type', 'other_device_type', 
            'brand', 'model', 'issue_description', 'resolve_description', 
            'status'  # Exclude 'date_received' and 'updated_at'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='col-md-6'),  # Device Name
                Column('contact', css_class='col-md-6'),  # Contact Information
            ),
            Row(
                Column('device_type', css_class='col-md-6'),  # Device Type
                Column('other_device_type', css_class='col-md-6', id='other-device-type'),  # Other Device Type
            ),
            Row(
                Column('brand', css_class='col-md-6'),  # Brand
                Column('model', css_class='col-md-6'),  # Model
            ),
            'issue_description',  # Issue Description (full width)
            'resolve_description',  # Resolve Description (full width)
            'status',  # Status (full width)
        )