from django.db import models

# Create your models here.


class Veblog(models.Model):
    title = models.CharField(max_length=50,verbose_name="عنوان وبلاگ")
    discription = models.TextField(max_length=500,null=True,blank=True,verbose_name="توضیحات وبلاگ")
    date = models.DateTimeField(null=True,blank=True,verbose_name="تاریخ انتشار وبلاگ")
    type = models.TextField(null=True,blank=True,verbose_name="نوع وبلاگ")
    image = models.ImageField(null=True,blank=True,upload_to="veblog_image",verbose_name="عکس وبلاگ")




    def __str__(self):
        return self.title