from django.urls import path
from . import views

app_name = 'course'
urlpatterns = [
    path("courselist/", views.ListCourseView.as_view(), name="courselist"),
    path("coursearchive/", views.ArchiveCourseView.as_view(), name="coursearchive"),
    path("courselist/search/", views.SearchCourseView.as_view(), name="search"),
    path('<int:id>', views.CourseDetailView.as_view(), name="course_taki"),
    path('category/<int:id>', views.CategoryCourseView.as_view(), name="category_course")

]
