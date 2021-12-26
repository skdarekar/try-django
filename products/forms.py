from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    title = forms.CharField(
        label='Product title',
        widget=forms.TextInput(
            attrs={
                'placeholder': "Your title"
            }
        )
    )
    email = forms.EmailField();
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
    class Meta(object):
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title");
        if "admin" not in title:
            raise forms.ValidationError("This is not a valid title")
        return title;

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email");
        if not email.endswith('.com'):
            raise forms.ValidationError("This is not a valid email")
        return email;
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
