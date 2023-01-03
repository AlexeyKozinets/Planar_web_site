# Generated by Django 4.1.4 on 2023-01-03 08:43

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0006_equipment_accessory_specifications_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment_item',
            name='specifications',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Технические характеристики'),
        ),
        migrations.AlterField(
            model_name='equipment_item',
            name='specifications_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Технические характеристики'),
        ),
        migrations.AlterField(
            model_name='equipment_item',
            name='specifications_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Технические характеристики'),
        ),
    ]
