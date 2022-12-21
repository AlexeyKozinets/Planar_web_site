from django.db import models
from django.contrib.auth.models import AbstractUser
from main_site.models import Company
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=False, null=True, verbose_name = _('Комания'))
    slug = models.SlugField(max_length=150, unique=True, db_index=True, verbose_name="URL",null=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = _('Пользователи')

