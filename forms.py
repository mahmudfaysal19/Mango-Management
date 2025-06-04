from django import forms
from .models import MangoExport

class MangoExportForm(forms.ModelForm):
    class Meta:
        model = MangoExport
        fields = ['category', 'description', 'price', 'quantity', 'availability']

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is None or price <= 0:
            raise forms.ValidationError('Price must be greater than zero.')
        return price

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity is None or quantity <= 0:
            raise forms.ValidationError('Quantity must be greater than zero.')
        return quantity