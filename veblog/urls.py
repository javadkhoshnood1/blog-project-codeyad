from django.urls import path
from . import views
app_name = "veblog"
urlpatterns = [
    path('',views.veblog_page_view ,name='list'),
    path('<int:id>',views.veblog_taki_page_view,name="taki")
]