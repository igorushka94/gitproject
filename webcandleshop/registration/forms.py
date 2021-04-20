from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User


class SignUpForm(UserChangeForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Ваше имя')
    last_name = forms.CharField(max_length=30, required=False, help_text='Ваша фамилия')
    email = forms.EmailField(max_length=254, help_text='Введите Ваш email')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', ) 