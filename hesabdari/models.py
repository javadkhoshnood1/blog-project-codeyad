from django.db import models
from django.urls import reverse
from jalali_date import datetime2jalali, date2jalali

from .managers import CustomerManagers


# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name="اسم محصول موجو د ")
    price_product = models.DecimalField(max_digits=10, decimal_places=3, null=True, verbose_name="قیمت واحد محصول")

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=100, null=True, verbose_name="نام و نام خانوادگی مشتری")
    phone_number = models.IntegerField(null=True, verbose_name="شماره تماس مشتری")
    all_costs = models.DecimalField(max_digits=10, decimal_places=3, null=True, verbose_name="کل یدهی مشتری")
    date = models.DateTimeField(null=True, auto_now=True, verbose_name="آخرین زمان خرید مشتری")
    product = models.ManyToManyField(Product, verbose_name="اسامی محصولات خرید کرده ")

    # objects = CustomerManagers() شخصی سازی متدها

    def get_absolote_url(self):
        return reverse("hesabdari:coustomer_taki", args=[self.id])

    def delete_customer_url(self):
        return reverse("hesabdari:dalatecustomer", args=[self.id])

    def get_created_costomer(self):
        return datetime2jalali(self.date)

    def __str__(self):
        return f"{self.phone_number} << {self.name}"
