from django.shortcuts import render
from .models import Coach
# Create your views here.

def coachs_page_view(request):
    coachs = Coach.objects.all()
    return render(request,'coach/coachlits.html',context={'coachs' : coachs})




def coach_taki_view(request,id):
    coach_taki = Coach.objects.get(id=id)
    return render(request,'coach/coach_taki.html',context={"coach" : coach_taki})

