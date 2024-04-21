from django.shortcuts import render
from .models import Veblog
# Create your views here.


def veblog_page_view(request):
    veblogs= Veblog.objects.all()
    return render(request,'veblog/veblog_list.html',context={"veblogs" : veblogs})