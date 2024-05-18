from django.urls import path
from . import views

app_name = "veblog"
urlpatterns = [
    path('', views.VeblogListView.as_view(), name='list'),
    path('category/<int:id>', views.CategoryVeblogView.as_view(), name="category_veblogs"),
    path('<int:id>', views.VeblogDetailView.as_view(), name="taki")
]
