from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BurtguulehForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        labels={'username':'Хэрэглэгчийн нэр',
                'password1': 'Нууц үг',
                'password2': 'Нууц үг давтах'}