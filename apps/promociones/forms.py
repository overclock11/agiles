from django import forms
from .models import *
from django.contrib.auth.models import User as AuthUser

class AuthUserForm(forms.ModelForm):
    class Meta:
        model = AuthUser
        fields = ['first_name', 'last_name', 'email']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['photo', 'country', 'city', 'address']

class CreateUser(forms.ModelForm):
      class Meta:
        model = User
        fields = [
                  'photo',
                  'country',
                  'city',
                  'address'
        ]

class UserCreatForm(forms.ModelForm):
    class Meta:
        model = AuthUser
        fields = ['first_name', 'last_name', 'email', 'username', 'password']


class CommentForm(forms.ModelForm):
    comment = forms.Textarea()
    class Meta:
        model = Commentary
        fields = ['email','comment']