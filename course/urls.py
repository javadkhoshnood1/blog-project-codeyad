from django.urls import path
from . import views

app_name = 'course'
urlpatterns = [
    path("courselist/", views.courselist_page_view, name="courselist"),
    path("courselist/search/", views.search_course, name="search"),
    path('<int:id>', views.course_taki_page_view, name="course_taki"),
    path('category/<int:id>', views.category_course_view, name="category_course")

]
