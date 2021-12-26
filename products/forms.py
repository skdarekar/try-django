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
    title = forms.CharField(
        label='Product title',
        widget=forms.TextInput(
            attrs={
                'placeholder': "Your title"
            }
        )
    )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'placeholder': "Your description",
                'class': "new-class two",
                'id': 'my-id',
                'rows': 3,
                'cols': 22
            }
        )
    )
    price = forms.DecimalField(initial=99.99)
