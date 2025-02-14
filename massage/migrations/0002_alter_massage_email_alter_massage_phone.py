# Generated by Django 5.0.3 on 2024-04-25 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('massage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='massage',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='ایمیل کاربر'),
        ),
        migrations.AlterField(
            model_name='massage',
            name='phone',
            field=models.CharField(max_length=13, unique=True, verbose_name='شماره تماس'),
        ),
    ]
