from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Coach
from django.core.paginator import Paginator


# Create your views here.


class CoachListView(ListView):
    template_name = 'coach/coachlits.html'
    context_object_name = "coachs"
    model = Coach
    paginate_by = 4


#
# def coachs_page_view(request):
#     coachs = Coach.objects.all()
#     paginator = Paginator(coachs,4)
#     page_number = request.GET.get("page")
#     coach_list = paginator.get_page(page_number)
#     return render(request,'coach/coachlits.html',context={'coachs' : coach_list})


def coach_taki_view(request, id):
    coach_taki = Coach.objects.get(id=id)
    return render(request, 'coach/coach_taki.html', context={"coach": coach_taki})


class CoachDetailView(DetailView):
    model = Coach
    pk_url_kwarg = "id"
    template_name = "coach/coach_taki.html"
    context_object_name = "coach"
