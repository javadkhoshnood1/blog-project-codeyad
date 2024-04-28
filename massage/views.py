from django.shortcuts import render,redirect
from .models import Massage



# Create your views here.


def massage_list_Page_View(request):
    massages = Massage.objects.all()
    return render(request, 'massage/massage_list.html', {"massages": massages})


def massage_add_page_view(request):
    if request.method == "POST":
        title = request.POST.get('title')
        discription = request.POST.get('discription')
        number = request.POST.get('phone')
        email = request.POST.get('email')
        new_massage = Massage.objects.create(title=title,discription=discription,phone=number,email=email)
        new_massage.save()
        return redirect('massage:massage_list')


    return render(request, 'massage/massage_add.html')




def massage_delete_view(request,id):
    delete_massage = Massage.objects.get(id=id)
    delete_massage.delete()
    return redirect('massage:massage_list')

