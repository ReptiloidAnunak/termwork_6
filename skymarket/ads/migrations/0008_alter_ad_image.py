# Generated by Django 3.2.6 on 2023-07-05 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0007_alter_comment_ad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='image',
            field=models.ImageField(blank=True, default=None, help_text='Разместите фото для объявления', null=True, upload_to='images/', verbose_name='Фото'),
        ),
    ]