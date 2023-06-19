from django import forms
from .models import Book,Category

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'category','year']
        labels = {
            'title': 'Номын нэр',
            'author': 'Зохиогч',
            'category': 'Төрөл',
            'year': 'Он'
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'year': forms.NumberInput(attrs={'class': 'form-control'}),
        }
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        labels= {'name':'Төрлийн нэр'}
