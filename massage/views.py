from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView

from .models import Massage
from .forms import SendMassage


# Create your views here.
class MassageListView(ListView):
    template_name = "massage/massage_list.html"
    model = Massage
    context_object_name = "massages"


# def massage_list_Page_View(request):
#     massages = Massage.objects.all()
#     return render(request, 'massage/massage_list.html', {"massages": massages})


class MassageAddView(FormView):
    template_name = "massage/massage_add.html"
    form_class = SendMassage
    success_url = reverse_lazy("massage:massage_list")

    def form_valid(self, form):
        data = form.cleaned_data
        Massage.objects.create(title=data["title"], discription=data["discription"], email=data["email"],
                               phone=data["phonenumber"])
        return super().form_valid(form)


# def massage_add_page_view(request):
#     if request.method == "POST":
#         form = SendMassage(request.POST)
#         if form.is_valid():
#             Massage.objects.create(title=form.cleaned_data["title"], discription=form.cleaned_data["discription"],
#                                    email=form.cleaned_data["email"], phone=form.cleaned_data["phonenumber"])
#             return redirect("massage:massage_list")
#     else:
#         form = SendMassage()
#     # if request.method == "POST":
#     #     title = request.POST.get('title')
#     #     discription = request.POST.get('discription')
#     #     number = request.POST.get('phone')
#     #     email = request.POST.get('email')
#     #     new_massage = Massage.objects.create(title=title,discription=discription,phone=number,email=email)
#     #     new_massage.save()
#     #     return redirect('massage:massage_list')
#
#     return render(request, 'massage/massage_add.html', context={"form": form})


def massage_delete_view(request, id):
    delete_massage = Massage.objects.get(id=id)
    delete_massage.delete()
    return redirect('massage:massage_list')
