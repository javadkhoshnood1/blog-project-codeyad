from django.shortcuts import render, redirect
from django.urls import reverse

from coach.models import Coach
from course.models import Course
from veblog.models import Veblog
from course.models import Category


# Create your views here.


def home_page_view(request):
    coachs = Coach.objects.all()[0:3]
    
    courses = Course.objects.all()[0:3]
    veblogs = Veblog.objects.all()[0:3]
    category_courses = Category.objects.all()
    return render(request, 'home/home_page.html',
                  context={"category_courses": category_courses, "coachs": coachs, "courses": courses,
                           "veblogs": veblogs})
