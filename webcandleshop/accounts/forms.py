from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput) 
    """ Виджет PasswordInput, будет сформирован в HTML как 
    элемент <input> с атрибутом type="password", поэтому 
    браузер будет работать с ним как с полем пароля """


# class UserRegistrationForm(forms.ModelForm):
#     """ Класс регистрации пользователя """
#     password = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

#     class Meta:
#         model = 'Пользователь'
#         field = ('username', 'first_name', 'email')

#     def clean_password2(self):
#         cd = self.cleaned_data
#         if cd['password'] != cd['password2']:
#             raise forms.ValidationError('Passwords don\'t match.')
#         return cd['password2']