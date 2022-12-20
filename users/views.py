from django.shortcuts import render, redirect
from users.models import CustomUser
from users.forms import CustomUserCreationForm, CustomPasswordChangeForm
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import PasswordChangeView

# Create your views here.

class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('Main_site:edit_list', kwargs={ 'modelId': 1 })
    template_name = 'signup.html'



class SignUpEdit(UpdateView):
    model = CustomUser
    fields = [  'company',
                'username',
                'is_active',
            ]
    success_url = reverse_lazy('Main_site:edit_list', kwargs={ 'modelId': 1 })
    template_name = 'signup.html'



class SignUpEditPassword(PasswordChangeView):
    model = CustomPasswordChangeForm
    success_url = reverse_lazy('Main_site:home')
    template_name = 'signup.html'




