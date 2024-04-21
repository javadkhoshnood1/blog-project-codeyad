from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model

user = get_user_model()


# Create your views here.


def login_view(request):
    # if request.user.is_authenticated :
    #     user_site = request.user.first_name
    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/", )
        else:
            return HttpResponse(f"user not found with this username {username} and password {password}")

    return render(request, 'acounts/login_page.html', )


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("/")


def signin_view(request):
    context = {"erors": []}
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        if password1 != password2:
            context["erors"].append("! رمز عبور شما مشابه یکدگر نیست ")
            return render(request, 'acounts/sigin_page.html', context=context)

        new_user = user.objects.create(username=username, email=email, password=password1)
        login(request, new_user)
        return redirect('/')

    return render(request, 'acounts/sigin_page.html')
