from django.urls import path
from . import views


app_name = 'coach'
urlpatterns =[
    path('coachlist/',views.coachs_page_view ,name="chechlist"),
    path("<int:id>",views.coach_taki_view,name="coach_taki")
]