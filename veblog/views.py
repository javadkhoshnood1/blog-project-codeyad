from django.shortcuts import render
from .models import Veblog
# Create your views here.


def veblog_page_view(request):
    veblogs= Veblog.objects.all().order_by("-title")
    return render(request,'veblog/veblog_list.html',context={"veblogs" : veblogs})




def veblog_taki_page_view(request,id):
    veblog= Veblog.objects.get(id=id)
    return render(request,'veblog/veblog_taki.html',context={"veblog" : veblog})

