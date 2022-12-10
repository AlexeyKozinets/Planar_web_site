from django.db import models
from django.contrib.auth.models import AbstractUser
from main_site.models import Company

class CustomUser(AbstractUser):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=False, null=True, verbose_name = 'Комания')


    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

