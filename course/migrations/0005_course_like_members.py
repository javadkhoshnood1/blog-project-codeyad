# Generated by Django 5.0.3 on 2024-04-23 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_remove_course_number_cousre'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='like_members',
            field=models.TextField(blank=True, max_length=20, null=True, verbose_name='میزان رضایت'),
        ),
    ]
