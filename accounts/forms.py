from typing import Any, Dict 
from django import forms
from .models import Users
from django.core.exceptions import ValidationError


class RegistForm(forms.ModelForm):
    user_name = forms.CharField(label='名前')
    email = forms.EmailField(label='メールアドレス')
    tel_number = forms.CharField(label='電話番号')
    address = forms.CharField(label='住所')
    regular_holiday = forms.ChoiceField(choices=Users.select_holiday, label='定休日')
    business_hours = forms.CharField(label='営業時間')
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='パスワード再入力', widget=forms.PasswordInput())

    class Meta:
        model = Users
        fields = ['user_name', 'email','tel_number', 'address', 'regular_holiday', 'business_hours', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise ValidationError('パスワードが一致しません')
            
    def save(self):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get("password"))
        user.save()
        return user
    
class UserLoginForm(forms.Form):
    email = forms.EmailField(label='メールアドレス')
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())