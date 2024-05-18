from dataclasses import field

from django.db import models


class Massage(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True, verbose_name="عنوان پیام")

    discription = models.TextField(max_length=300, null=True, blank=True, verbose_name="توضیحات پیام ")

    email = models.EmailField(null=True, blank=True, verbose_name="ایمیل کاربر", unique=True)

    phone = models.CharField(max_length=13, null=False, blank=False, unique=True, verbose_name="شماره تماس", )

    class Meta:
        verbose_name = "پیام"
        verbose_name_plural = "پیام ها "

    def __str__(self):
        return self.title