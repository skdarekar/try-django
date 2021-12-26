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
            