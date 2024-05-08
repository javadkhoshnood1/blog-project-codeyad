from django.contrib import admin
from .models import Course, Category, Comment

# Register your models here.


admin.site.register(Course)
admin.site.register(Category)
admin.site.register(Comment)
