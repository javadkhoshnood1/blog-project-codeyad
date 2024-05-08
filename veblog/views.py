from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import Veblog, Category, Comment
from django.core.paginator import Paginator


# Create your views here.
def veblog_category(request, id=None):
    all_category = Category.objects.all()
    category = get_object_or_404(Category, id=id)
    category_name = category.title
    category_veblog = category.veblog_set.all()
    return render(request, 'veblog/veblog_list.html',
                  {"veblogs": category_veblog, "all_category": all_category, 'category_name': category_name})


def veblog_page_view(request):
    veblogs = Veblog.objects.all().order_by("-title")
    all_category = Category.objects.all()
    paginator = Paginator(veblogs, 6)
    page_number = request.GET.get("page")
    veblog_list = paginator.get_page(page_number)
    return render(request, 'veblog/veblog_list.html', context={"veblogs": veblog_list, "all_category": all_category})


def veblog_taki_page_view(request, id):
    veblog = Veblog.objects.get(id=id)
    if request.method == 'POST':
        massage = request.POST.get('message')
        idd = request.POST.get('parent_id')

        if massage:
            Comment.objects.create(user=request.user, body=massage, vrblog=veblog, reply_comment_id=idd)
    return render(request, 'veblog/veblog_taki.html', context={"veblog": veblog})
