from django.urls import path
from . import views

app_name = "massage"
urlpatterns = [
    path('list/', views.massage_list_Page_View, name="massage_list"),
    path('add/', views.massage_add_page_view, name="massage_add"),
    path('delete/<int:id>', views.massage_delete_view, name="massage_del"),
]
