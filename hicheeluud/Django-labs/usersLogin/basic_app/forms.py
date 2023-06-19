from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password =  forms.CharField(label='Нууц үг',widget=forms.PasswordInput(attrs={'class': 'narrow-input', 'required': 'true' }), required=True, help_text='Password must be 8 characters minimum length (with at least 1 lower case, 1 upper case and 1 number).')
    password2 = forms.CharField(label='Нууц үг давтах',widget=forms.PasswordInput(attrs={'class': 'narrow-input', 'required': 'true' }), required=True,)
    class Meta():
        model = User
        fields = ['username', 'email', 'password','password2']
        labels = {'username':'Хэрэглэгчийн нэр',
                  'email': 'Email хаяг'}
class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ['user_site', 'user_pic']
        labels = {'user_site':'Линк',
                  'user_pic': 'Зураг'}
