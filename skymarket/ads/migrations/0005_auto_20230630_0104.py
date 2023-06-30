# Generated by Django 3.2.6 on 2023-06-30 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0004_auto_20230630_0059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='', verbose_name='Дата создания'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ad',
            name='description',
            field=models.CharField(default='', help_text='Введите описание товара', max_length=1000, verbose_name='Описание товара'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ad',
            name='image',
            field=models.ImageField(default=' ', help_text='Разместите фото для объявления', upload_to='images/', verbose_name='Фото'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ad',
            name='price',
            field=models.PositiveIntegerField(default=0, help_text='Добавьте цену товара', verbose_name='Цена товара'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='title',
            field=models.CharField(default=' ', help_text='Введите название товара', max_length=200, verbose_name='Название товара'),
            preserve_default=False,
        ),
    ]
