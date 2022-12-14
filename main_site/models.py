from random import choices
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _ # <-- for translation of verbose names

class Company(models.Model):
    company_name = models.CharField(blank = False, max_length = 150, verbose_name = 'Название комании')
    is_published = models.BooleanField(default=True, verbose_name = 'Отображение')

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = 'Наименование команий'
        verbose_name_plural = 'Наименования компаний'
        ordering = ['company_name',]

class Equipment_Class(models.Model):
    #which have name of holding
    company = models.ForeignKey('Company', on_delete=models.CASCADE, verbose_name = _('Комания'))
    class_name = models.CharField(blank = False, max_length = 150, verbose_name = _('Название'))
    short_description =  models.CharField(blank = False,max_length = 150, verbose_name = _('Предназанчение'))
    full_description = models.TextField(blank = False, max_length = 1500, verbose_name = _('Полное описание'))
    img = models.ImageField(upload_to = 'equipment_class_uploads', verbose_name = 'Изображение', null=True, blank=True)
    is_published = models.BooleanField(default=True, verbose_name = 'Отображение')

    def __str__(self):
        return self.class_name

    class Meta:
        verbose_name = 'Класс оборудования'
        verbose_name_plural = _('Классы оборудования')
        ordering = ['class_name',]


class Equipment_Category(models.Model):
    #refference to class (one to many)
    company = models.ForeignKey('Company', on_delete=models.CASCADE, verbose_name = 'Комания')
    equipment_class = models.ForeignKey('Equipment_Class', on_delete=models.CASCADE, verbose_name = 'Класс')
    category_name = models.CharField(max_length=150, blank=False, verbose_name='Название')
    short_description =  models.CharField(blank = False,max_length = 150, verbose_name = 'Предназанчение')
    full_description = models.TextField(blank = False, max_length = 1500, verbose_name = 'Полное описание')
    is_published = models.BooleanField(default=True, verbose_name = 'Отображение')



    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Категория оборудования'
        verbose_name_plural = _('Категории оборудования')
        ordering = ['category_name',]


class Equipment_Item(models.Model):
    #refference to category (one to many)
    company = models.ForeignKey('Company', on_delete=models.CASCADE, verbose_name = 'Комания')
    equipment_class = models.ForeignKey('Equipment_Class', on_delete=models.CASCADE, verbose_name = 'Класс')
    equipment_category = models.ForeignKey('Equipment_Category', on_delete=models.CASCADE, verbose_name = 'Категория')
    item_name = models.CharField(max_length=150, blank=False, verbose_name='Название')
    short_description =  models.CharField(blank = False,max_length = 150, verbose_name = 'Предназанчение')
    full_description = models.TextField(blank = False, max_length = 1500, verbose_name = 'Полное описание')
    is_published = models.BooleanField(default=True, verbose_name = 'Отображение')
    pass

    def __str__(self):
            return self.item_name

    class Meta:
        verbose_name = 'Наименование оборудования'
        verbose_name_plural = _('Наименования оборудования')
        ordering = ['item_name',]

class Equipment_Acessory(models.Model):
    #refference to items (many to many)
    company = models.ForeignKey('Company', on_delete=models.CASCADE,verbose_name = 'Комания')
    equipment = models.ManyToManyField('Equipment_Item', verbose_name='Oборудование')
    acessory_name = models.CharField(max_length=150, blank=False, verbose_name='Название')
    short_description =  models.CharField(blank = False,max_length = 150, verbose_name = 'Предназанчение')
    full_description = models.TextField(blank = False, max_length = 1500, verbose_name = 'Полное описание')
    is_published = models.BooleanField(default=True, verbose_name = 'Отображение')

    def __str__(self):
        return self.acessory_name

    class Meta:
        verbose_name = 'Наименование аксессуара'
        verbose_name_plural = _('Наименования аксессуаров')
        ordering = ['acessory_name',]
