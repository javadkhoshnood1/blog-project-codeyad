from django.contrib import admin
from .models import Veblog, Category,Comment

# Register your models here.

admin.site.register(Veblog)
admin.site.register(Category)
admin.site.register(Comment)

