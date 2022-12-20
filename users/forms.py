from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from users.models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('company', 'username',)


class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = CustomUser
        fields = ("old_password", "new_password1", "new_password2")


