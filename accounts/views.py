from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def register(request):
    if  request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')

        if password1 == password2 :
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already exists")
                return redirect("register")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already exists")
                return redirect("register")
            else :
                user = User.objects.create_user(username=username, email=email, password=password1, first_name=fname, last_name=lname)
                user.save()
                messages.info(request,"User registered succesfully")
                return redirect("login")
        else:
            messages.info(request,"incorrect password")
        print(password1,password2)
    return render(request,"accounts/register.html")


def login(request):
    if  request.user.is_authenticated:
        return redirect("home")
    print("request.method==>",request.method)
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = auth.authenticate(username = username,password = password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,"invalid crudentials")
    return render(request,"accounts/login.html")


def logout(request):
    auth.logout(request)
    return render(request,"accounts/login.html")

@login_required(login_url='login')
def home(request):
    
    return render(request,"accounts/test.html")
