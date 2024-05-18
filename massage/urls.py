from django.urls import path
from . import views

app_name = "massage"
urlpatterns = [
    path('list/', views.MassageListView.as_view(), name="massage_list"),
    path('add/', views.MassageAddView.as_view(), name="massage_add"),
    path('delete/<int:id>', views.massage_delete_view, name="massage_del"),
]
