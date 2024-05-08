from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.shortcuts import redirect
from django.urls import reverse
from jalali_date import datetime2jalali


class Category(models.Model):
    title = models.CharField(null=True, blank=True, max_length=80, verbose_name="دسته بندی درور ها ")
    discription = models.TextField(max_length=100, verbose_name="توضیحات دسته بندی ها ", null=True, blank=True)

    def __str__(self):
        return self.title


class Course(models.Model):
    date = models.DateField(auto_now=True, )
    title = models.TextField(max_length=50, null=True, blank=True, verbose_name="عنوان دوره")
    discription = models.TextField(max_length=200, null=True, blank=True, verbose_name="توضیحات دوره")
    time_course = models.IntegerField(null=True, blank=True, verbose_name="مدت زمان دوره")
    type = models.ManyToManyField(Category, blank=True, verbose_name="دسته بندی دور ه ")
    teacher = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="استاده دوره ")
    price_course = models.IntegerField(null=True, blank=True, verbose_name="هزینه دوره ")
    image_course = models.ImageField(upload_to="image_course", null=True, blank=True, verbose_name="عکس دوره ")
    like_members = models.TextField(max_length=20, default="عالی", null=True, blank=True, verbose_name="میزان رضایت")
    numbers_members = models.IntegerField(null=True, blank=True, verbose_name=" تعداد دانسجویان دروه ")

    def get_absolote_url(self):
        return reverse("course:course_taki", args=[self.id])

    def __str__(self):
        return self.title


class Comment(models.Model):
    body = models.TextField(max_length=200, null=True, blank=True, verbose_name="متن کامنت دوره")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name="نام کاربر")
    date = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ارسال نظر")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True, verbose_name="برای دوره ")

    def get_date(self):
        return datetime2jalali(self.date)
