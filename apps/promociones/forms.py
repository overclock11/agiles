from django import forms
from .models import *
from django.contrib.auth.models import User as AuthUser

class AuthUserForm(forms.ModelForm):
    class Meta:
        model = AuthUser
        fields = ('first_name', 'last_name', 'email')

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('photo', 'country', 'city', 'address')