# Generated by Django 5.0.3 on 2024-04-21 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coach', '0002_alter_coach_course_number_alter_coach_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coach',
            name='image_coach',
            field=models.ImageField(blank=True, null=True, upload_to='coach_image', verbose_name='عکس کاربر'),
        ),
    ]
