from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from .forms import LoginForm, SignIn, EditProfile

user = get_user_model()


# Create your views here.


def edit_profile(request):
    form = EditProfile(instance=request.user)
    if request.method == "POST":
        form = EditProfile(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            print("sddd")
            return redirect("home:main")

    return render(request, 'acounts/edit_profile.html', {"form": form})


def login_view(request):
    form = LoginForm()
    # if request.user.is_authenticated :
    #     user_site = request.user.first_name
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            print(username, password)
            login_user = authenticate(request, username=username, password=password)
            print(login_user)
            if login_user is not None:
                login(request, login_user)
                print("login")
                return redirect("home:main")

    return render(request, 'acounts/login_page.html', {"form": form})


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("/")


def signin_view(request):
    if request.method == 'POST':
        form = SignIn(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            new_user = user.objects.create(username=username, email=email, password=password)
            login(request, new_user)
            return redirect('/')
    else:
        form = SignIn()

    return render(request, 'acounts/sigin_page.html', {"form": form})
