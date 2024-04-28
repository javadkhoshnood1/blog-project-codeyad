from django.shortcuts import render
from .models import Course


# Create your views here.


def courselist_page_view(request):
    courses = Course.objects.all().order_by("title")
    for course in courses:
        if int(course.numbers_members) >= 50:
            course.like_members = "عالی"

        else:
            course.like_members = "معمولی"

    return render(request, 'course/courselist.html', context={"courses": courses})


def course_taki_page_view(request, id):
    course = Course.objects.get(id=id)
    if int(course.numbers_members) >= 50:
        course.like_members = "عالی"

    else:
        course.like_members = "معمولی"

    course.save()



    return render(request, 'course/course_taki.html', context={"course": course})



