from django.urls import path
from . import views
app_name = "veblog"
urlpatterns = [
    path('',views.veblog_page_view ,name='list')
]