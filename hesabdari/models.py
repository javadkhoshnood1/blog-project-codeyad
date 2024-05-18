from django.db import models
from django.urls import reverse
from django.utils.html import format_html
from jalali_date import datetime2jalali, date2jalali
from django.core.validators import MinValueValidator, MaxValueValidator

from .managers import CustomerManagers


# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name="اسم محصول موجود ")
    image = models.ImageField(upload_to="products_image", null=True, blank=True, verbose_name="عکس محصول")

    price_product = models.BigIntegerField(default=0, null=True, blank=True, verbose_name="قیمت واحد محصول")
    percent_price = models.IntegerField(validators=[MinValueValidator(0),
                                                    MaxValueValidator(100)], default=0, null=True, blank=True,
                                        verbose_name="تخفیف محصول")

    def __str__(self):
        return self.name

    def upload_image(self):
        return format_html(f'<img src="{self.image.url}" alt="javad" width="50px" height="50px">')

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = 'محصولات فروشگاه'


class Customer(models.Model):
    name = models.CharField(max_length=100, null=True, verbose_name="نام و نام خانوادگی مشتری")
    phone_number = models.IntegerField(null=True, verbose_name="شماره تماس مشتری")
    all_costs = models.BigIntegerField(null=True, verbose_name="کل یدهی مشتری", blank=True)
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

    class Meta:
        verbose_name = "مشتری"
        verbose_name_plural = 'مشتریان فروشگاه'
