import email
from pickle import NONE
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def login_request(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "account/login.html", {
                "error": "username or password is valid"
            })

    return render(request, "account/login.html")

def register_request(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        # firstname = request.POST["firstname"]
        # lastname = request.POST["lastname"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]

        if password == repassword:
            if User.objects.filter(username=username).exists():
                return render(request, "account/register.html", 
                {
                    "error":"This username has already registered",
                    "username":username,
                    "email":email,
                    # "firstname":firstname,
                    # "lastname":lastname
                })
            else:
                if User.objects.filter(email=email).exists():
                    return render(request, "account/register.html", 
                    {
                        "error":"This email has already registered","username":username,
                        "email":email,
                        # "firstname":firstname,
                        # "lastname":lastname
                    })
                else:
                    user = User.objects.create_user(username=username,email=email,
                    password=password)
                    user.save()
                    login(request, user)
                    return redirect ("home")

        else:
            return render(request, "account/register.html", 
                {
                    "error":"password doeesn't match",
                    "username":username,
                    "email":email,
                })


    return render(request, "account/register.html")

def logout_request(request):
    logout(request)
    return redirect("home")

