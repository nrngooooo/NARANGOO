from django import forms
from django.forms import ModelForm
from categoryApp.models import Category
from itemApp.models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('price',)
        labels = {
            'id':'Код',
            'bname':'Барааны нэр',
            'price': 'Барааны үнэ',
            'category': 'Ангилал'
        }
class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        labels = {
            'id':'Код',
            'cname':'Төрлийн нэр',
        }