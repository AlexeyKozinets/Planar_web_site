from random import choices
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _ # <-- for translation of verbose names
from django_unique_slugify import unique_slugify #<- installed module
from random import randint


class Company(models.Model):
    company_name = models.CharField(blank = False, max_length = 150, verbose_name = 'Название комании')
    slug = models.SlugField(max_length=150, unique=True, db_index=True, verbose_name="URL")
    is_published = models.BooleanField(default=True, verbose_name = 'Отображение')

    def save(self, *args, **kwargs):  # new
        rand_code = ''.join([ chr([randint(48,57), randint(65,90), 45][randint(0,2)]) for i in range(randint(8,12))])
        unique_slugify(self, self.company_name_en + '-' + rand_code)
        #=====================================================(altrernate way without import)
        # if not self.slug:
        #     self.slug = slugify(self.company_name_en)     ##[from django.utils.text import slugify] <- onboard slugify import##

        # for i in range(1,999):
        #     if Company.objects.filter(slug=self.slug).exists() and len(self.slug) == len(slugify(self.company_name_en)):
        #         self.slug = slugify(self.company_name_en + '-' + str(i))
        #     else:
        #         break
        #====================================================================================
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = 'Наименование команий'
        verbose_name_plural = _('Наименования компаний')
        ordering = ['company_name',]

class Equipment_Class(models.Model):
    #which have name of holding
    company = models.ForeignKey('Company', on_delete=models.CASCADE, verbose_name = _('Комания'))
    class_name = models.CharField(blank = False, max_length = 150, verbose_name = _('Название'))
    slug = models.SlugField(max_length=150, unique=True, db_index=True, verbose_name="URL")
    short_description =  models.CharField(blank = False,max_length = 150, verbose_name = _('Предназанчение'))
    full_description = models.TextField(blank = False, max_length = 1500, verbose_name = _('Полное описание'))
    img = models.ImageField(upload_to = 'equipment_class_uploads', verbose_name = 'Изображение', null=True, blank=True)
    is_published = models.BooleanField(default=True, verbose_name = 'Отображение')

    def save(self, *args, **kwargs):  # new
        rand_code = ''.join([ chr([randint(48,57), randint(65,90), 45][randint(0,2)]) for i in range(randint(8,12))])
        unique_slugify(self, self.class_name_en + '-' + rand_code)
        return super().save(*args, **kwargs)

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
    slug = models.SlugField(max_length=150, unique=True, db_index=True, verbose_name="URL")
    short_description =  models.CharField(blank = False,max_length = 150, verbose_name = 'Предназанчение')
    full_description = models.TextField(blank = False, max_length = 1500, verbose_name = 'Полное описание')
    is_published = models.BooleanField(default=True, verbose_name = 'Отображение')

    def save(self, *args, **kwargs):
        rand_code = ''.join([ chr([randint(48,57), randint(65,90), 45][randint(0,2)]) for i in range(randint(8,12))])
        unique_slugify(self, self.category_name_en + '-' + rand_code)
        return super().save(*args, **kwargs)

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
    slug = models.SlugField(max_length=150, unique=True, db_index=True, verbose_name="URL")
    short_description =  models.CharField(blank = False,max_length = 150, verbose_name = 'Предназанчение')
    full_description = models.TextField(blank = False, max_length = 1500, verbose_name = 'Полное описание')
    is_published = models.BooleanField(default=True, verbose_name = 'Отображение')
    pass

    def save(self, *args, **kwargs):  # new
        rand_code = ''.join([ chr([randint(48,57), randint(65,90), 45][randint(0,2)]) for i in range(randint(8,12))])
        unique_slugify(self, self.item_name_en + '-' + rand_code)
        return super().save(*args, **kwargs)

    def __str__(self):
            return self.item_name

    class Meta:
        verbose_name = 'Наименование оборудования'
        verbose_name_plural = _('Наименования оборудования')
        ordering = ['item_name',]

class Equipment_Accessory(models.Model):
    #refference to items (many to many)
    company = models.ForeignKey('Company', on_delete=models.CASCADE,verbose_name = 'Комания')
    equipment = models.ManyToManyField('Equipment_Item', verbose_name='Oборудование')
    accessory_name = models.CharField(max_length=150, blank=False, verbose_name='Название')
    slug = models.SlugField(max_length=150, unique=True, db_index=True, verbose_name="URL")
    short_description =  models.CharField(blank = False,max_length = 150, verbose_name = 'Предназанчение')
    full_description = models.TextField(blank = False, max_length = 1500, verbose_name = 'Полное описание')
    is_published = models.BooleanField(default=True, verbose_name = 'Отображение')

    def save(self, *args, **kwargs):  # new
        rand_code = ''.join([ chr([randint(48,57), randint(65,90), 45][randint(0,2)]) for i in range(randint(8,12))])
        unique_slugify(self, self.accessory_name_en + '-' + rand_code)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.accessory_name

    class Meta:
        verbose_name = 'Наименование аксессуара'
        verbose_name_plural = _('Наименования аксессуаров')
        ordering = ['accessory_name',]
