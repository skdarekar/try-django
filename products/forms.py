from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    class Meta(object):
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

class RowProductForm(forms.Form):
    title = forms.CharField()  
    description = forms.CharField()
    price = forms.DecimalField()