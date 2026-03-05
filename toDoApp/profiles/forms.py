from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth import get_user_model


CustomUser = get_user_model()


class ToDoUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("username", "email",)


class ToDoUserChangeForm(UserChangeForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("username", "email", "password1", "password2")


class ToDoUserLoginForm(AuthenticationForm):
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'placeholder': 'Email'}),
        label='Email',
    )

    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Username'}),
        label='Username',
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
        label='Password',
    )

