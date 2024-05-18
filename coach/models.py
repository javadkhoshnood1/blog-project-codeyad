from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.urls import reverse


class Coach(models.Model):
    name = models.CharField(max_length=35, null=True, blank=True, verbose_name="نام و نام خانوادگی")
    work_type = models.TextField(max_length=80, null=True, blank=True, verbose_name="نوع فغالیت ")
    course_number = models.IntegerField(null=True, blank=True, verbose_name="تعداد دوره مربی")
    student_number = models.IntegerField(null=True, blank=True, verbose_name="تعداد دانشجوی مربی")
    email = models.EmailField(max_length=60, null=True, blank=True, verbose_name="یمیل مربی")
    number = models.IntegerField(null=True, blank=True, verbose_name='شمماره تماس')
    image_coach = models.ImageField(upload_to='coach_image', null=True, blank=True, verbose_name="عکس کاربر")
    like = models.IntegerField(default=5, verbose_name="تعداد لایک مربی")

    def __str__(self):
        return self.name

    def get_absolote_url(self):
        return reverse("coach:coach_taki", args=[self.id])

    class Meta:
        verbose_name = "مربی "
        verbose_name_plural = "مربی ها"
