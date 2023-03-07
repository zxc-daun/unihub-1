
from django.utils.translation import gettext as _
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError

from .models import *


class RegisterForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("User with this username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("User with this email already exists")
        return email

    def clean(self):
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise forms.ValidationError("Passwords don't match")
        return self.cleaned_data

    def save(self):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password']
        )
        return user


class NewRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True, help_text='Required. Enter your username.')
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.')
    first_name = forms.CharField(max_length=30, required=True, help_text='Required. Enter your first name.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required. Enter your last name.')

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email", "password1", "password2")
        field_classes = {'email': forms.EmailField}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            if field:
                field.widget.attrs.update({'class': 'form-control'})
        self.fields['email'].required = True

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class CustomAuthenticationForm(AuthenticationForm):
    username_or_email = forms.CharField(
        label=_('Username or Email'),
        widget=forms.TextInput(attrs={'autofocus': True}),
        error_messages={
            'required': _('Please enter your username or email address.'),
        }
    )
    password = forms.CharField(
        label=_('Password'),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
        error_messages={
            'required': _('Please enter your password.'),
        },
    )

    def clean(self):
        cleaned_data = super().clean()
        username_or_email = cleaned_data.get('username_or_email')
        password = cleaned_data.get('password')

        if username_or_email and password:
            # Authenticate user based on your custom user model
            user = authenticate(username_or_email=username_or_email, password=password)
            if user is None:
                raise forms.ValidationError(_('Invalid username/email or password'))

        return cleaned_data
