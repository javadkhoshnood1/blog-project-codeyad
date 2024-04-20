from django.shortcuts import render

# Create your views here.


def login_view(request):
    if request.method == "POST":
        print(f"{request.POST.get('username')} agelehhhh {request.POST.get('password')}")
    return render(request,'acounts/login_page.html')
