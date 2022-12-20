from django.db import models
from django.contrib.auth.models import AbstractUser
from main_site.models import Company
from django_unique_slugify import unique_slugify #<- installed module
from random import randint

class CustomUser(AbstractUser):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=False, null=True, verbose_name = 'Комания')
    slug = models.SlugField(max_length=150, unique=True, db_index=True, verbose_name="URL",null=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

