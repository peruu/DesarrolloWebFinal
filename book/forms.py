from django import forms
from django.forms import ModelForm
from book.models import *

class GenreForm(forms.ModelForm):
    adventure = forms.BooleanField()
    class Meta:
<<<<<<< HEAD
        model = Book
        fields = [
            'title',
        	'author', 
        	'editorial', 
        	'book_type', 
        	'genre', 
        	'language', 
        	'original', 
        	'transaction', 
        	'price', 
        	'comment', 
        	'number_of_pages', 
        	'picture',
        ]

=======
        model = Genre
        fields = '__all__'
        labels = {
            'adventure': 'Aventura',
        }
        widgets = {
            'adventure': forms.widgets.CheckboxInput(),
        }