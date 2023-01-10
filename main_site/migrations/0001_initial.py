# Generated by Django 4.1.1 on 2023-01-06 08:29

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=150, verbose_name='Название')),
                ('company_name_ru', models.CharField(max_length=150, null=True, verbose_name='Название')),
                ('company_name_en', models.CharField(max_length=150, null=True, verbose_name='Название')),
                ('slug', models.SlugField(max_length=150, unique=True, verbose_name='URL')),
                ('company_head_img', models.ImageField(blank=True, null=True, upload_to='companies_uploads', verbose_name='Главное изображение')),
                ('is_published', models.BooleanField(default=True, help_text='Отображение данных на странице сайта.', verbose_name='Отображение')),
                ('priority', models.DecimalField(decimal_places=0, help_text='Определяет очередность отображения информации на странице сайта (1 - 99).', max_digits=2, verbose_name='Приоритет отображения')),
            ],
            options={
                'verbose_name': 'Комания',
                'verbose_name_plural': 'Компании',
                'ordering': ['company_name'],
            },
        ),
        migrations.CreateModel(
            name='Equipment_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=150, verbose_name='Название')),
                ('category_name_ru', models.CharField(max_length=150, null=True, verbose_name='Название')),
                ('category_name_en', models.CharField(max_length=150, null=True, verbose_name='Название')),
                ('slug', models.SlugField(max_length=150, unique=True, verbose_name='URL')),
                ('short_description', models.CharField(max_length=150, verbose_name='Предназанчение')),
                ('short_description_ru', models.CharField(max_length=150, null=True, verbose_name='Предназанчение')),
                ('short_description_en', models.CharField(max_length=150, null=True, verbose_name='Предназанчение')),
                ('full_description', models.TextField(max_length=1500, verbose_name='Полное описание')),
                ('full_description_ru', models.TextField(max_length=1500, null=True, verbose_name='Полное описание')),
                ('full_description_en', models.TextField(max_length=1500, null=True, verbose_name='Полное описание')),
                ('product_head_img', models.ImageField(blank=True, help_text='Изображение класса, категории или самой продукции (если не выбрано, то используется "зашлушка")', null=True, upload_to='categories_uploads', verbose_name='Главное изображение')),
                ('is_published', models.BooleanField(default=True, help_text='Отображение данных на странице сайта.', verbose_name='Предназанчение')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_site.company', verbose_name='Комания')),
            ],
            options={
                'verbose_name': 'Категория данных',
                'verbose_name_plural': 'Категории данных',
                'ordering': ['category_name'],
            },
        ),
        migrations.CreateModel(
            name='Equipment_Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=150, verbose_name='Название')),
                ('class_name_ru', models.CharField(max_length=150, null=True, verbose_name='Название')),
                ('class_name_en', models.CharField(max_length=150, null=True, verbose_name='Название')),
                ('slug', models.SlugField(max_length=150, unique=True, verbose_name='URL')),
                ('short_description', models.CharField(max_length=150, verbose_name='Предназанчение')),
                ('short_description_ru', models.CharField(max_length=150, null=True, verbose_name='Предназанчение')),
                ('short_description_en', models.CharField(max_length=150, null=True, verbose_name='Предназанчение')),
                ('full_description', models.TextField(max_length=1500, verbose_name='Полное описание')),
                ('full_description_ru', models.TextField(max_length=1500, null=True, verbose_name='Полное описание')),
                ('full_description_en', models.TextField(max_length=1500, null=True, verbose_name='Полное описание')),
                ('product_head_img', models.ImageField(blank=True, help_text='Изображение класса, категории или самой продукции (если не выбрано, то используется "зашлушка")', null=True, upload_to='classes_uploads', verbose_name='Главное изображение')),
                ('is_published', models.BooleanField(default=True, help_text='Отображение данных на странице сайта.', verbose_name='Отображение')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_site.company', verbose_name='Комания')),
            ],
            options={
                'verbose_name': 'Класс данных',
                'verbose_name_plural': 'Классы данных',
                'ordering': ['class_name'],
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_head_img', models.ImageField(upload_to='news_uploads', verbose_name='Заглавное изображение в новости')),
                ('title', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('title_ru', models.CharField(max_length=150, null=True, verbose_name='Заголовок')),
                ('title_en', models.CharField(max_length=150, null=True, verbose_name='Заголовок')),
                ('slug', models.SlugField(max_length=150, unique=True, verbose_name='URL')),
                ('body1', ckeditor.fields.RichTextField(blank=True, help_text='Тескт статьи до карусели дополнительных изображений', null=True, verbose_name='Содержание статьи')),
                ('body1_ru', ckeditor.fields.RichTextField(blank=True, help_text='Тескт статьи до карусели дополнительных изображений', null=True, verbose_name='Содержание статьи')),
                ('body1_en', ckeditor.fields.RichTextField(blank=True, help_text='Тескт статьи до карусели дополнительных изображений', null=True, verbose_name='Содержание статьи')),
                ('body2', ckeditor.fields.RichTextField(blank=True, help_text='Тескт статьи после карусели дополнительных изображений', null=True, verbose_name='Содержание статьи')),
                ('body2_ru', ckeditor.fields.RichTextField(blank=True, help_text='Тескт статьи после карусели дополнительных изображений', null=True, verbose_name='Содержание статьи')),
                ('body2_en', ckeditor.fields.RichTextField(blank=True, help_text='Тескт статьи после карусели дополнительных изображений', null=True, verbose_name='Содержание статьи')),
                ('file', models.FileField(blank=True, null=True, upload_to='news_uploads')),
                ('issued', models.DateTimeField()),
                ('is_published', models.BooleanField(default=True, help_text='Отображение данных на странице сайта.', verbose_name='Отображение')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_site.company', verbose_name='Комания')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
                'ordering': ['issued'],
            },
        ),
        migrations.CreateModel(
            name='News_Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('additional_imgs', models.ImageField(upload_to='news_uploads', verbose_name='Дополнительные изображения в новости')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_site.news', verbose_name='Новость')),
            ],
        ),
        migrations.CreateModel(
            name='Equipment_Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=150, verbose_name='Oборудование')),
                ('item_name_ru', models.CharField(max_length=150, null=True, verbose_name='Oборудование')),
                ('item_name_en', models.CharField(max_length=150, null=True, verbose_name='Oборудование')),
                ('slug', models.SlugField(max_length=150, unique=True, verbose_name='URL')),
                ('short_description', models.CharField(max_length=150, verbose_name='Предназанчение')),
                ('short_description_ru', models.CharField(max_length=150, null=True, verbose_name='Предназанчение')),
                ('short_description_en', models.CharField(max_length=150, null=True, verbose_name='Предназанчение')),
                ('full_description', models.TextField(max_length=1500, verbose_name='Полное описание')),
                ('full_description_ru', models.TextField(max_length=1500, null=True, verbose_name='Полное описание')),
                ('full_description_en', models.TextField(max_length=1500, null=True, verbose_name='Полное описание')),
                ('specifications', ckeditor.fields.RichTextField(null=True, verbose_name='Технические характеристики')),
                ('specifications_ru', ckeditor.fields.RichTextField(null=True, verbose_name='Технические характеристики')),
                ('specifications_en', ckeditor.fields.RichTextField(null=True, verbose_name='Технические характеристики')),
                ('product_head_img', models.ImageField(blank=True, help_text='Изображение класса, категории или самой продукции (если не выбрано, то используется "зашлушка")', null=True, upload_to='objects_uploads', verbose_name='Главное изображение')),
                ('is_published', models.BooleanField(default=True, help_text='Отображение данных на странице сайта.', verbose_name='Отображение')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_site.company', verbose_name='Комания')),
                ('equipment_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_site.equipment_category', verbose_name='Категория')),
                ('equipment_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_site.equipment_class', verbose_name='Класс')),
            ],
            options={
                'verbose_name': 'Объект данных',
                'verbose_name_plural': 'Объекты данных',
                'ordering': ['item_name'],
            },
        ),
        migrations.AddField(
            model_name='equipment_category',
            name='equipment_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_site.equipment_class', verbose_name='Класс'),
        ),
        migrations.CreateModel(
            name='Equipment_Accessory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accessory_name', models.CharField(max_length=150, verbose_name='Название')),
                ('accessory_name_ru', models.CharField(max_length=150, null=True, verbose_name='Название')),
                ('accessory_name_en', models.CharField(max_length=150, null=True, verbose_name='Название')),
                ('slug', models.SlugField(max_length=150, unique=True, verbose_name='URL')),
                ('short_description', models.CharField(max_length=150, verbose_name='Предназанчение')),
                ('short_description_ru', models.CharField(max_length=150, null=True, verbose_name='Предназанчение')),
                ('short_description_en', models.CharField(max_length=150, null=True, verbose_name='Предназанчение')),
                ('full_description', models.TextField(max_length=1500, verbose_name='Полное описание')),
                ('full_description_ru', models.TextField(max_length=1500, null=True, verbose_name='Полное описание')),
                ('full_description_en', models.TextField(max_length=1500, null=True, verbose_name='Полное описание')),
                ('specifications', models.TextField(blank=True, max_length=3000, null=True, verbose_name='Технические характеристики')),
                ('specifications_ru', models.TextField(blank=True, max_length=3000, null=True, verbose_name='Технические характеристики')),
                ('specifications_en', models.TextField(blank=True, max_length=3000, null=True, verbose_name='Технические характеристики')),
                ('product_head_img', models.ImageField(blank=True, help_text='Изображение класса, категории или самой продукции (если не выбрано, то используется "зашлушка")', null=True, upload_to='attributes_uploads', verbose_name='Главное изображение')),
                ('is_published', models.BooleanField(default=True, help_text='Отображение данных на странице сайта.', verbose_name='Отображение')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_site.company', verbose_name='Комания')),
                ('equipment', models.ManyToManyField(to='main_site.equipment_item', verbose_name='Oборудование')),
            ],
            options={
                'verbose_name': 'Атрибут объекта',
                'verbose_name_plural': 'Атрибуты объектов',
                'ordering': ['accessory_name'],
            },
        ),
    ]