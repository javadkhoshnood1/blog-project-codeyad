# Generated by Django 5.0.3 on 2024-04-21 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=35, null=True, verbose_name='نام و نام خانوادگی')),
                ('work_type', models.TextField(blank=True, max_length=80, null=True, verbose_name='نوع فغالیت ')),
                ('course_number', models.IntegerField(blank=True, max_length=5, null=True, verbose_name='تعداد دوره مربی')),
                ('student_number', models.IntegerField(blank=True, max_length=10, null=True, verbose_name='تعداد دانشجوی مربی')),
                ('email', models.EmailField(blank=True, max_length=60, null=True, verbose_name='یمیل مربی')),
                ('number', models.IntegerField(blank=True, max_length=10, null=True, verbose_name='شمماره تماس')),
                ('image_coach', models.ImageField(blank=True, null=True, upload_to='coach_image', verbose_name='کس کاربر')),
            ],
        ),
    ]
