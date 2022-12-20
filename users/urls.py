
from django.urls import path
from users import views

app_name = 'Users'
urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signUp'),
    path('signup/edit:<int:pk>', views.SignUpEdit.as_view(), name='signUpEdit'),
    path('signup/edit_pass:<int:pk>', views.SignUpEditPassword.as_view(), name='signUpEditPass'),

    

]
