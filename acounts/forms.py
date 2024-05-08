from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "input100", "placeholder": "enter yor username"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "input100", "placeholder": "enter yor password"}))


class SignIn(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "input100", "placeholder": "enter you username"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "input100", "placeholder": "enter you email"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "input100", "placeholder": "enter you apssword"}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "input100", "placeholder": "enter you password2"}))

    def clean(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password != password2:
            raise ValidationError("passwords not sames")


class EditProfile(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")
