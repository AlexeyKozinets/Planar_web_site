from django.shortcuts import render, redirect, get_object_or_404
from users.models import CustomUser
from users.forms import CustomUserCreationForm, CustomUserChangeForm, CustomPasswordChangeForm
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView


# Create your views here.

class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('Main_site:edit_list', kwargs={ 'modelId': 1 })
    template_name = 'signup.html'




def SignUpEditMult(request,pk):
    # https://openclassrooms.com/en/courses/7107341-intermediate-django/7264795-include-multiple-forms-on-a-page
    if request.user.is_authenticated:
        editable = get_object_or_404(CustomUser, id=pk)
        user_form = CustomUserChangeForm(instance=editable)
        password_form = CustomPasswordChangeForm(pk)
        if request.method == 'POST':
            if 'company' in request.POST:
                user_form = CustomUserChangeForm(request.POST, instance=editable)
                if user_form.is_valid():
                    user_form.save()
                    return redirect(reverse('Users:signUpEditMult', kwargs={ 'pk': pk }))
            if 'company' not in request.POST:
                # https://pylessons.com/django-handle-password
                password_form = CustomPasswordChangeForm(editable, request.POST)
                if password_form.is_valid():
                    password_form.save()
                    return redirect(reverse('Users:signUpEditMult', kwargs={ 'pk': pk }))
        context = {
            'user_form': user_form,
            'password_form': password_form,
        }
        return render(request, 'edit_sign.html', context)
    else:
        return redirect('Main_site:home')

