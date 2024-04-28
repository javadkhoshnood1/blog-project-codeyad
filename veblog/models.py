from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# on-delete => casecade- set_null - set_default - do_nothing

# Choise = (
#     ('A',"برنامه نویسی"),
#     ('B',"طراحی سایت با المنتور"),
#     ('C' ,'طراحی سایت با جنگو'),
#     ('D' ,"گرافیک")
#
# )
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=100)
    created = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Veblog(models.Model):
    title = models.CharField(max_length=50, verbose_name="عنوان وبلاگ")
    discription = models.TextField(max_length=500, null=True, blank=True, verbose_name="توضیحات وبلاگ")
    aouter = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name="نویسنده بلاگ", null=True,
                               blank=True)  # many to one
    created = models.DateTimeField(auto_now=True,null=True,verbose_name="تاریخ انتشار وبلاگ")
    updated = models.DateTimeField(auto_now_add=True,null=True, verbose_name="تاریخ به روز رسانی وبلاگ")

    type = models.ManyToManyField(Category, verbose_name=" دسته بندی ها")
    image = models.ImageField(null=True, blank=True, upload_to="veblog_image", verbose_name="عکس وبلاگ")




    def get_absolote_url(self):
        return reverse("veblog:taki",args=[self.id])




    def __str__(self):
        return self.title






