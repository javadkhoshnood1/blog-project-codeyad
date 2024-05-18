from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView

from .models import Veblog, Category, Comment


class CategoryVeblogView(DetailView):
    model = Category
    template_name = "veblog/veblog_list.html"
    pk_url_kwarg = "id"

    def get_context_data(self, **kwargs):
        context = super(CategoryVeblogView, self).get_context_data()
        context["all_category"] = Category.objects.all()
        category = Category.objects.get(id=self.kwargs["id"])
        context["veblogs"] = category.veblog_set.all()
        context["category_name"] = category.title
        return context


# # Create your views here.
# def veblog_category(request, id=None):
#     all_category = Category.objects.all()
#     category = get_object_or_404(Category, id=id)
#     category_name = category.title
#     category_veblog = category.veblog_set.all()
#     return render(request, 'veblog/veblog_list.html',
#                   {"veblogs": category_veblog, "all_category": all_category, 'category_name': category_name})


class VeblogListView(ListView):
    template_name = "veblog/veblog_list.html"
    paginate_by = 6
    model = Veblog
    context_object_name = "veblogs"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["all_category"] = Category.objects.all()
        return context


#
# def veblog_page_view(request):
#     veblogs = Veblog.objects.all().order_by("-title")
#     all_category = Category.objects.all()
#     paginator = Paginator(veblogs, 6)
#     page_number = request.GET.get("page")
#     veblog_list = paginator.get_page(page_number)
#     return render(request, 'veblog/veblog_list.html', context={"veblogs": veblog_list, "all_category": all_category})


# def veblog_taki_page_view(request, id):
#     veblog = Veblog.objects.get(id=id)
#     if request.method == 'POST':
#         massage = request.POST.get('message')
#         idd = request.POST.get('parent_id')
#
#         if massage:
#             Comment.objects.create(user=request.user, body=massage, vrblog=veblog, reply_comment_id=idd)
#     return render(request, 'veblog/veblog_taki.html', context={"veblog": veblog})


class VeblogDetailView(DetailView):
    model = Veblog
    template_name = "veblog/veblog_taki.html"
    pk_url_kwarg = "id"
    context_object_name = "veblog"

    def post(self, request, *args, **kwargs):
        massage = request.POST.get('message')
        idd = request.POST.get('parent_id')
        vrblog = Veblog.objects.get(id=self.kwargs["id"])
        if massage:
            Comment.objects.create(user=request.user, body=massage, vrblog=vrblog,
                                   reply_comment_id=idd)

        return render(request, 'veblog/veblog_taki.html', context={"veblog": vrblog})
