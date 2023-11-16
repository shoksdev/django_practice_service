from django import forms
from django.core.exceptions import ValidationError

from .models import CustomUser


class RegistrationUserForm(forms.ModelForm):
    password2 = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput,
                                help_text='Введите пароль ещё раз')
    consent = forms.BooleanField(label='Согласие на обработку данных', widget=forms.CheckboxInput,)

    def clean(self):
        super().clean()
        password1 = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            errors = {'password2': ValidationError('Введённые пароли не совпадают', code='password_mismatch')}
            raise ValidationError(errors)



    class Meta:
        model = CustomUser
        fields = ('full_name', 'username', 'email', 'password', 'password2', 'consent',)
