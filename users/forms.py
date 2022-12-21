from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from users.models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('company', 'username', 'first_name', 'last_name', 'email',)


class CustomUserChangeForm(forms.ModelForm):
    # https://stackoverflow.com/questions/61208760/how-to-remove-no-password-set-on-my-django-template-for-editing-a-profile
    class Meta:
        model = CustomUser
        fields = ('company', 'username', 'first_name', 'last_name', 'email', 'is_active',)


class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = CustomUser
        fields = ("old_password", "new_password1", "new_password2")


