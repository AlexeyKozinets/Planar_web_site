from django.db import models
from django_unique_slugify import unique_slugify #<- installed module
from random import randint
from Planar.model_verbose_transtatios import *
from ckeditor.fields import RichTextField


class Company(models.Model):
    company_name = models.CharField(blank = False, max_length = 150, verbose_name = name_verb)
    slug = models.SlugField(max_length=150, unique=True, db_index=True, verbose_name="URL")
    company_head_img = models.ImageField(upload_to = 'companies_uploads', verbose_name = img_verb,)
    is_published = models.BooleanField(default=True, verbose_name = showing_verb, help_text = publishing_help)
    priority = models.DecimalField(blank = False, max_digits = 2, decimal_places=0, verbose_name = priority_verb, help_text = priority_help)

    def save(self, *args, **kwargs):  # new
        if not Company.objects.filter(slug=self.slug).exists() or not self.is_published:
            rand_code = ''.join([ chr([randint(48,57), randint(65,90), 45][randint(0,2)]) for i in range(randint(8,12))])
            unique_slugify(self, self.company_name_en + '-' + rand_code)
        return super().save(*args, **kwargs)
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
        verbose_name = company_meta_verb
        verbose_name_plural = company_meta_verb_plr
        ordering = ['company_name',]

class Equipment_Class(models.Model):
    #which have name of holding
    company = models.ForeignKey('Company', on_delete=models.CASCADE, verbose_name = company_verb)
    class_name = models.CharField(blank = False, max_length = 150, verbose_name = name_verb)
    slug = models.SlugField(max_length=150, unique=True, db_index=True, verbose_name="URL")
    short_description =  models.CharField(blank = False,max_length = 150, verbose_name = short_verb)
    full_description = RichTextField(blank = False, verbose_name = full_verb)
    product_head_img = models.ImageField(upload_to = 'classes_uploads', null=True, blank=True, verbose_name = img_verb, help_text = product_head_img_help)
    is_published = models.BooleanField(default=True, verbose_name = showing_verb, help_text = publishing_help)

    def save(self, *args, **kwargs):
        if not Equipment_Class.objects.filter(slug=self.slug).exists() or not self.is_published:
            rand_code = ''.join([ chr([randint(48,57), randint(65,90), 45][randint(0,2)]) for i in range(randint(8,12))])
            unique_slugify(self, self.class_name_en + '-' + rand_code)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.class_name

    class Meta:
        verbose_name = class_meta_verb
        verbose_name_plural = class_meta_verb_plr
        ordering = ['class_name',]


class Equipment_Category(models.Model):
    #refference to class (one to many)
    company = models.ForeignKey('Company', on_delete=models.CASCADE, verbose_name = company_verb)
    equipment_class = models.ForeignKey('Equipment_Class', on_delete=models.CASCADE, verbose_name = class_verb)
    category_name = models.CharField(max_length=150, blank=False, verbose_name = name_verb)
    slug = models.SlugField(max_length=150, unique=True, db_index=True, verbose_name="URL")
    short_description =  models.CharField(blank = False,max_length = 150, verbose_name = short_verb)
    full_description = RichTextField(blank = False, verbose_name = full_verb)
    product_head_img = models.ImageField(upload_to = 'categories_uploads', null=True, blank=True, verbose_name = img_verb, help_text = product_head_img_help)
    is_published = models.BooleanField(default=True, verbose_name = short_verb, help_text = publishing_help)

    def save(self, *args, **kwargs):
        if not Equipment_Category.objects.filter(slug=self.slug).exists() or not self.is_published:
            rand_code = ''.join([ chr([randint(48,57), randint(65,90), 45][randint(0,2)]) for i in range(randint(8,12))])
            unique_slugify(self, self.category_name_en + '-' + rand_code)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = category_meta_verb
        verbose_name_plural = category_meta_verb_plr
        ordering = ['category_name',]


class Equipment_Item(models.Model):
    #refference to category (one to many)
    company = models.ForeignKey('Company', on_delete=models.CASCADE, verbose_name = company_verb)
    equipment_class = models.ForeignKey('Equipment_Class', on_delete=models.CASCADE, verbose_name = class_verb)
    equipment_category = models.ForeignKey('Equipment_Category', on_delete=models.CASCADE, verbose_name = category_verb)
    item_name = models.CharField(max_length=150, blank=False, verbose_name = item_verb)
    slug = models.SlugField(max_length=150, unique=True, db_index=True, verbose_name="URL")
    short_description =  models.CharField(blank = False,max_length = 150, verbose_name = short_verb)
    full_description = RichTextField(blank = False, verbose_name = full_verb)
    specifications = RichTextField(blank = False, null=True, verbose_name = spec_verb)
    product_head_img = models.ImageField(upload_to = 'objects_uploads', null=True, blank=True, verbose_name = img_verb, help_text = product_head_img_help)
    is_published = models.BooleanField(default=True, verbose_name = showing_verb, help_text = publishing_help)
    pass

    def save(self, *args, **kwargs):  # new
        if not Equipment_Item.objects.filter(slug=self.slug).exists() or not self.is_published:
            rand_code = ''.join([ chr([randint(48,57), randint(65,90), 45][randint(0,2)]) for i in range(randint(8,12))])
            unique_slugify(self, self.item_name_en + '-' + rand_code)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.item_name

    class Meta:
        verbose_name = item_meta_verb
        verbose_name_plural = item_meta_verb_plr
        ordering = ['item_name',]

class Equipment_Accessory(models.Model):
    #refference to items (many to many)
    company = models.ForeignKey('Company', on_delete=models.CASCADE,verbose_name = company_verb)
    equipment = models.ManyToManyField('Equipment_Item', verbose_name = item_verb)
    accessory_name = models.CharField(max_length=150, blank=False, verbose_name = name_verb)
    slug = models.SlugField(max_length=150, unique=True, db_index=True, verbose_name="URL")
    short_description =  models.CharField(blank = False,max_length = 150, verbose_name = short_verb)
    full_description = RichTextField(blank = False, verbose_name = full_verb)
    specifications = RichTextField(blank = True, null=True, verbose_name = spec_verb)
    product_head_img = models.ImageField(upload_to = 'attributes_uploads', null=True, blank=True, verbose_name = img_verb, help_text = product_head_img_help)
    is_published = models.BooleanField(default=True, verbose_name = showing_verb, help_text = publishing_help)

    def save(self, *args, **kwargs):  # new
        if not Equipment_Accessory.objects.filter(slug=self.slug).exists() or not self.is_published:
            rand_code = ''.join([ chr([randint(48,57), randint(65,90), 45][randint(0,2)]) for i in range(randint(8,12))])
            unique_slugify(self, self.accessory_name_en + '-' + rand_code)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.accessory_name

    class Meta:
        verbose_name = accessory_meta_verb
        verbose_name_plural = accessory_meta_verb_plr
        ordering = ['accessory_name',]

class News(models.Model):
    company = models.ForeignKey('Company', on_delete=models.CASCADE,verbose_name = company_verb)
    news_head_img = models.ImageField(upload_to = 'news_uploads', blank=False, verbose_name = news_head_img_verb,)
    title = models.CharField(max_length=150, blank=False, verbose_name = title_verb)
    slug = models.SlugField(max_length=150, unique=True, db_index=True, verbose_name="URL")
    body1 = RichTextField(blank = True, null=True, verbose_name = body_verb, help_text = body_1_help)
    body2 = RichTextField(blank = True, null=True, verbose_name = body_verb, help_text = body_2_help)
    file = models.FileField(upload_to ='news_uploads',null=True,blank=True)
    issued = models.DateTimeField(blank=False)
    is_published = models.BooleanField(default=True, verbose_name = showing_verb, help_text = publishing_help)

    def save(self, *args, **kwargs):  # new
        if not News.objects.filter(slug=self.slug).exists() or not self.is_published:
            rand_code = ''.join([ chr([randint(48,57), randint(65,90), 45][randint(0,2)]) for i in range(randint(8,12))])
            unique_slugify(self, self.title_en + '-' + rand_code)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = news_meta_verb
        verbose_name_plural = news_meta_verb_plr
        ordering = ['issued',]

#need make additional views, url paths and templates with custom forms fiels
class News_Images(models.Model):
    news = models.ForeignKey('News', on_delete=models.CASCADE, verbose_name=news_verb)
    additional_imgs = models.ImageField(upload_to='news_uploads', blank=True ,verbose_name=additional_imgs_verb)

    def __str__(self):
        return self.news.title



class Contacts(models.Model):
    company = models.ForeignKey('Company', on_delete=models.CASCADE,verbose_name = company_verb)
    slug = models.SlugField(max_length=150, unique=True, db_index=True, verbose_name="URL")
    contact_data = RichTextField(blank = True, null=True, verbose_name = contacts_verb)
    is_published = models.BooleanField(default=True, verbose_name = showing_verb, help_text = publishing_help)

    def save(self, *args, **kwargs):  # new
        if not Contacts.objects.filter(slug=self.slug).exists() or not self.is_published:
            rand_code = ''.join([ chr([randint(48,57), randint(65,90), 45][randint(0,2)]) for i in range(randint(8,12))])
            unique_slugify(self, self.company.company_name + '-contacts-' + rand_code)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.company

    class Meta:
        verbose_name = contacts_meta_verb
        verbose_name_plural = contacts_meta_verb_plr
        ordering = ['company',]




