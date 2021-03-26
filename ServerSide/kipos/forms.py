from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import KiposUser


class KiposUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length = 254, help_text = 'Required. Inform a valid email address.')

    def get_user(self):
        return self.user_cache

    class Meta:
        model = KiposUser
        fields = ("username", "email", "password1", "password2")
