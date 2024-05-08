from django import forms
from django.core.exceptions import ValidationError

from .models import Customer, Product


class AddCustomer(forms.Form):
    name = forms.CharField(max_length=50, label="نام مشتری")
    phonenumber = forms.IntegerField(label="شماره تماس")
    price = forms.IntegerField(widget=forms.TextInput(attrs={"value": "تومان0"}), disabled=True, required=False,
                               label="بدهی مشتری")

    def clean(self):
        name = self.cleaned_data["name"]
        for i in Customer.objects.all():
            if name == i.name:
                raise ValidationError("کابر با این اسم وجود دارد")


class AddProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "enter your name"
            }),
            "price_product": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "enter your price"
            })
        }

    def clean(self):
        name = self.cleaned_data["name"]
        for i in Product.objects.all():
            if name == i.name:
                raise ValidationError("product with this name is and change name")
