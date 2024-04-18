from django.shortcuts import render

# Create your views here.


def login_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(f"password,username{username} {password}")
    return render(request,'acounts/login_page.html')
