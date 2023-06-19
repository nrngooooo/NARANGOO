from django import forms
from django.forms import ModelChoiceField
from tenhimApp.models import Tenhim

class BagshForm(forms.Form):
    bovog = forms.CharField()
    bname = forms.CharField()
    email = forms.EmailField(widget=forms.EmailInput())
    tenhim = forms.ModelChoiceField(queryset=Tenhim.objects.all())
    password =  forms.CharField(widget=forms.PasswordInput(attrs={'class': 'narrow-input', 'required': 'true' }), required=True, help_text='Password must be 8 characters minimum length (with at least 1 lower case, 1 upper case and 1 number).')
    password_confirm = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'narrow-input', 'required': 'true' }), required=True, )