from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'description', 'price', 'contact_phone', 'location', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'contact_phone': forms.TextInput(attrs={'placeholder': 'e.g. +1234567890'}),
        }
    
    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise forms.ValidationError("Price must be greater than zero")
        return price