# Generated by Django 5.0.3 on 2024-04-27 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veblog', '0009_alter_veblog_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
