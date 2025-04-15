from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput)

# forms.py
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username", "password1", "password2"]
