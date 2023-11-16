from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser


class RegistrationUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput)
    email = forms.EmailField(label='Email', widget=forms.EmailInput)
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput)
    consent = forms.BooleanField(label='Согласие на обработку данных', widget=forms.CheckboxInput, )

    class Meta:
        model = CustomUser
        fields = ('full_name', 'username', 'email', 'password1', 'password2', 'consent',)
