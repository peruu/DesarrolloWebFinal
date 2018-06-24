from django import forms
from django.forms import ModelForm
from book.models import *

class GenreForm(forms.ModelForm):
    adventure = forms.BooleanField()
    class Meta:
        model = Genre
        fields = '__all__'
        labels = {
            'adventure': 'Aventura',
        }
        widgets = {
            'adventure': forms.widgets.CheckboxInput(),
        }