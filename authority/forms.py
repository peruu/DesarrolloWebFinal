from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class SignUpAdminForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Opcional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Opcional')
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']
        widgets = {
            'password': forms.PasswordInput(),
        }
