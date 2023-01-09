from django.db import models
from django.contrib.auth.models import AbstractUser
from main_site.models import Company
from Planar.model_verbose_transtatios import *

class CustomUser(AbstractUser): # <- this model name using in "edit_list.html"
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=False, null=True, verbose_name = company_verb)
    slug = models.SlugField(max_length=150, unique=True, db_index=True, verbose_name="URL",null=True)

    class Meta:
        verbose_name = user_meta_verb
        verbose_name_plural = user_meta_verb_plr

