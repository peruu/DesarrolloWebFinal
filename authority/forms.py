from django import forms
from django.forms import widgets
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# FAV_GENRE_CHOICES = (
#     ('FANTASY', "Fantasía"),
#     ('FICTION', "Ficción"),
#     ('HORROR', "Terror"),
#     ('ROMANTIC', "Romantico"),
#     ('None',"Ninguno"),
# )
class SignUpUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    RUN = forms.CharField(max_length=15)
    commune = forms.CharField(max_length=20)
    phone = forms.CharField(max_length=20)
    # choice_field = forms.ChoiceField( widget=widgets.RadioSelect,choices=FAV_GENRE_CHOICES)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']
        widgets = {
            'password': forms.PasswordInput(),
        }
