from django.urls import path
from . import views

app_name = 'coach'
urlpatterns = [
    path('coachlist/', views.CoachListView.as_view(), name="chechlist"),
    path("<int:id>", views.CoachDetailView.as_view(), name="coach_taki")
]
