from django.shortcuts import render
from .models import Coach
from django.core.paginator import Paginator
# Create your views here.

def coachs_page_view(request):
    coachs = Coach.objects.all()
    paginator = Paginator(coachs,4)
    page_number = request.GET.get("page")
    coach_list = paginator.get_page(page_number)
    return render(request,'coach/coachlits.html',context={'coachs' : coach_list})




def coach_taki_view(request,id):
    coach_taki = Coach.objects.get(id=id)
    return render(request,'coach/coach_taki.html',context={"coach" : coach_taki})

