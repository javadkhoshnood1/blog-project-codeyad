# Generated by Django 5.0.3 on 2024-04-23 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_course_numbers_members'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='like_members',
            field=models.TextField(blank=True, default='عالی', max_length=20, null=True, verbose_name='میزان رضایت'),
        ),
    ]
