from django import forms
from django.core.exceptions import ValidationError


class SendMassage(forms.Form):
    title = forms.CharField(max_length=50, label="title")
    discription = forms.CharField(max_length=200, label="discription")
    email = forms.EmailField(label="email")
    phonenumber = forms.IntegerField(label="phone number ")

    def clean(self):
        title = self.cleaned_data["title"]
        discription = self.cleaned_data["discription"]
        if title == discription:
            raise ValidationError("title same with discription", code="t_in_d")
