from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
            'summary',
            'active'
        ]

class RawProductForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "new-class-name two",
                "id": "my-id",
                "rows": 10,
                "cols": 120
            }
        )
    )
    price = forms.DecimalField(initial="9.99")