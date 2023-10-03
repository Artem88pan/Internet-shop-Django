from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput, error_messages={'required': 'заполните поле!'})
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
        help_texts = {
            'username': 'Только буквы, цифры и символы @/./+/-/_',
        }
        labels = {
            'username': 'Логин',
            'first_name': 'Имя пользователя',
            'email': 'почта',
        }
        verbose_name = {
            'username': 'login',
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('пароли не совпадают')
        return cd['password2']
    
class AuthForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True}),label=_("Логин"),)
    password = forms.CharField(label=_("Пароль"), strip=False, widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),)

    error_messages = {
        "invalid_login": _(
            "Пожалуйста введите коректные логин и пароль. Обратите внимание на то, что! "
            "поля могут быть чувствительны к регистру."
        ),
        "inactive": _("Этот аккаунт заблокирован."),
    }    