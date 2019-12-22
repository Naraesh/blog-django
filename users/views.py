from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
from django.contrib import messages
from django.http import HttpResponse


def registrationpage(request):
    return render(request,'register.html')   
def loginpage(request):
    return render(request,'login.html')

def login(request):
    if request.method=="POST":
        first_name = request.POST.get('username')
        pass1 = request.POST.get('password1')
        usr=auth.authenticate(username=first_name,password=pass1)
        if usr is not None:
            auth.login(request,usr)
            return render(request,'profile.html')
        else:
            messages.info(request,'something went wrong')
            return redirect('loginpage')
    else:
        return render(request, 'login.html')
def logout(request):
    auth.logout(request)
    return render(request,'login.html')

def register(request): 
    if request.method =='POST':
        Firstname=request.POST.get('firstname')
        Lastname=request.POST.get('lastname')
        Username=request.POST.get('username')
        Email = request.POST.get('mail')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if pass1==pass2:
            if User.objects.filter(username=Username).exists():
                messages.info(request,'username exists')
                return redirect('registrationpage')
            elif User.objects.filter(email=Email):
                messages.info(request, 'mail exists')
                return redirect('registrationpage')
            else:
                usr=User.objects.create_user(username=Username,first_name=Firstname,last_name=Lastname,email=Email,password=pass1)
                usr.save()
                return redirect('loginpage')
        else:
            messages.info(request, 'password wrong')
            return redirect('registrationpage')
    else:
        return render(request,'register.html')
