# -*- coding: utf-8 -*-

from django.forms import ModelForm
from Blog.models import Comments
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import get_user_model

__author__ = 'Anrew Zaharovskyi'


class CommentForm(ModelForm):
    class Meta():
        model = Comments
        fields = ['comments_text']


class UserCreationForm(forms.ModelForm):
    username = forms.CharField(
        label='User (login):',
        widget=forms.TextInput,
    )
    password1 = forms.CharField(
        label='Password:',
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Confirm password:',
        widget=forms.PasswordInput
    )
    first_name = forms.CharField(
        label='First name:',
        max_length=30,
        required=False
    )
    last_name = forms.CharField(
        label='Last name:',
        max_length=30,
        required=False
    )
    email = forms.EmailField(
        label='Email address:',
        widget=forms.EmailInput
    )

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Password and confirmation do not match')
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ('username',)
