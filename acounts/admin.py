from django.contrib import admin

from .models import ProfileUser

# Register your models here.
admin.site.register(ProfileUser)
admin.site.site_header = "جواد خشنود"
admin.site.site_title = "مدیریت فارسی"
admin.site.index_title = "الله یار باشد دشمن هزار باشد"
