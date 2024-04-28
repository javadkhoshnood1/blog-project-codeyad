from django.shortcuts import render

from coach.models import Coach
from course.models import Course
from veblog.models import Veblog

# Create your views here.
coachs = Coach.objects.all()[0:3]
courses = Course.objects.all()[0:3]
veblogs = Veblog.objects.all()[0:3]


def home_page_view(request):
    return render(request, 'home/home_page.html', context={"coachs": coachs, "courses": courses, "veblogs": veblogs})
