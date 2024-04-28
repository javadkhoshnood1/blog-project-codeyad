from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ProfileUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="اطلاعات کاربر")
    persian_code = models.CharField(max_length=10, verbose_name="کد ملی")
    image_user = models.ImageField(upload_to="image_user", null=True, blank=True, verbose_name="عکسک کاربر")


    def __str__(self):
        return self.persian_code
