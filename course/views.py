from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Course, Category, Comment


# Create your views here.


def search_course(request):
    category_list = Category.objects.all()
    search = request.GET.get("search")
    courses_search = Course.objects.filter(title__contains=search)
    return render(request, 'course/courselist.html',
                  context={'category_list': category_list, "courses": courses_search})


def category_course_view(request, id=None):
    category_list = Category.objects.all()
    category_id = Category.objects.get(id=id)
    category_name = category_id.title
    category_courses = category_id.course_set.all()
    return render(request, 'course/courselist.html',
                  context={'category_list': category_list, "category_name": category_name,
                           "courses": category_courses})


def courselist_page_view(request):
    category_list = Category.objects.all()
    courses = Course.objects.all().order_by("title")
    pagenator = Paginator(courses, 6)
    page_number = request.GET.get("page")
    courses_page = pagenator.get_page(page_number)
    for course in courses:
        if int(course.numbers_members) >= 50:
            course.like_members = "عالی"

        else:
            course.like_members = "معمولی"

    return render(request, 'course/courselist.html',
                  context={"courses": courses_page, 'category_list': category_list})


def course_taki_page_view(request, id):
    comment_all = Comment.objects
    course = Course.objects.get(id=id)
    if request.method == "POST":
        body = request.POST.get('body')
        if body:
            print(",fjdhfbuidufhdufhdi")
            Comment.objects.create(body=body, user=request.user, course=course)
    if int(course.numbers_members) >= 50:
        course.like_members = "عالی"

    else:
        course.like_members = "معمولی"

    course.save()

    return render(request, 'course/course_taki.html', context={"course": course, "comment": comment_all})
