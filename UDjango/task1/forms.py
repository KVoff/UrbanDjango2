from django import forms

class UserRegister(forms.Form):
    username = forms.CharField(max_length=30,
                               label='Введите логин')
    password = forms.CharField(min_length=8, max_length=30,
                               widget=forms.PasswordInput,
                               label='Введите пароль')
    confirm_password = forms.CharField(min_length=8, max_length=30,
                                       widget=forms.PasswordInput,
                                       label='Повторите пароль')
    age = forms.IntegerField(max_value=100, min_value=1,
                             label='Введите свой возраст')
