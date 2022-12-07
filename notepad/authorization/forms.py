from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms


class LoginUserForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "text",
        'autocomplete': 'off',
    }))

    password = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "password",
    }))


class RegisterUserForm(UserCreationForm):

    username = forms.CharField(label='form-label', widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "text",
        'autocomplete': 'off',

    }))

    password1 = forms.CharField(label='form-label', widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "password",


     }))

    password2 = forms.CharField(label='form-label', widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "password",

    }))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
