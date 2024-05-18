from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, DetailView, ArchiveIndexView
from django.views.generic.list import ListView
from .mixins import LoginRequierdUser
from .models import Course, Category, Comment


# Create your views here.

class SearchCourseView(ListView):
    template_name = "course/courselist.html"
    context_object_name = "list_courses"

    def get(self, request, *args, **kwargs):
        search_word = request.GET.get("search")
        course_search = Course.objects.filter(title__contains=search_word)
        return render(request, self.template_name,
                      {self.context_object_name: course_search, "list_category": Category.objects.all()})


# def search_course(request):
#     category_list = Category.objects.all()
#     search = request.GET.get("search")
#     courses_search = Course.objects.filter(title__contains=search)
#     return render(request, 'course/courselist.html',
#                   context={'category_list': category_list, "list_courses": courses_search})

class CategoryCourseView(DetailView):
    model = Category
    template_name = "course/courselist.html"
    context_object_name = "categoryyyy"
    pk_url_kwarg = "id"

    def get_context_data(self, **kwargs):
        context = super(CategoryCourseView, self).get_context_data()
        context["list_category"] = Category.objects.all()
        category_id = Category.objects.get(id=self.kwargs["id"])
        context["category_name"] = category_id.title
        context["list_courses"] = category_id.course_set.all()
        return context


#
# def category_course_view(request, id=None):
#     category_list = Category.objects.all()
#     category_id = Category.objects.get(id=id)
#     category_name = category_id.title
#     category_courses = category_id.course_set.all()
#     return render(request, 'course/courselist.html',
#                   context={'list_category': category_list, "category_name": category_name,
#                            "list_courses": category_courses})


class ListCourseView(ListView):
    model = Course
    context_object_name = "list_courses"
    paginate_by = 6
    template_name = "course/courselist.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex["list_category"] = Category.objects.all()
        return contex

    for course in Course.objects.all():
        if int(course.numbers_members) >= 50:
            course.like_members = "عالی"

        else:
            course.like_members = "معمولی"


class ArchiveCourseView(ArchiveIndexView):
    model = Course
    date_field = "date"

    context_object_name = "list_courses"
    paginate_by = 6
    template_name = "course/courselist.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex["list_category"] = Category.objects.all()

        return contex


# def courselist_page_view(request):
#     category_list = Category.objects.all()
#     courses = Course.objects.all().order_by("title")
#     pagenator = Paginator(courses, 6)
#     page_number = request.GET.get("page")
#     courses_page = pagenator.get_page(page_number)
#     for course in courses:
#         if int(course.numbers_members) >= 50:
#             course.like_members = "عالی"
#
#         else:
#             course.like_members = "معمولی"
#
#     return render(request, 'course/courselist.html',
#                   context={"courses": courses_page, 'category_list': category_list})


# def course_taki_page_view(request, id):
#     comment_all = Comment.objects.all()
#     course = Course.objects.get(id=id)
#     if request.method == "POST":
#         body = request.POST.get('body')
#         if body:
#             Comment.objects.create(body=body, user=request.user, course=course)
#     if int(course.numbers_members) >= 50:
#         course.like_members = "عالی"
#
#     else:
#         course.like_members = "معمولی"
#
#     course.save()
#
#     return render(request, 'course/course_taki.html', context={"course": course, "comment": comment_all})


class CourseDetailView(LoginRequierdUser, DetailView):
    model = Course
    template_name = "course/course_taki.html"
    pk_url_kwarg = "id"
    context_object_name = "course"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comment"] = Comment.objects.all()
        return context
