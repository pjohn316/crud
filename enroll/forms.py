from django.core import validators
from django import forms
from .models import User


class UserRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"

        widgets = {
            'fnames': forms.TextInput(attrs={'class': 'form-control'}),
            'lname': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(render_value=True, attrs={'class': 'form-control', 'placeholder': 'min 6 char'}),

        }
