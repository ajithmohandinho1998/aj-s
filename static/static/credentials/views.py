from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        uname=request.POST['userid']
        pwd=request.POST['password']
        user=auth.authenticate(username=uname,password=pwd)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"INVALID CREDENTIALS")
            return redirect('login')

    return render(request,"login.html")
def register(request):
    if request.method == 'POST':
        username=request.POST['uname']
        fname = request.POST['fname']
        lname = request.POST['lname']
        eid = request.POST['email']
        pwd = request.POST['pwd']
        pwd1 = request.POST['pwd1']

        if pwd==pwd1:
            if User.objects.filter(username=username).exists():
                messages.info(request,"USERNAME TAKEN")
                return redirect('register')
            elif User.objects.filter(email=eid).exists():
                messages.info(request,"EMAIL TAKEN")
                return redirect('register')
            else:

                user=User.objects.create_user(username=username,first_name=fname,last_name=lname,email=eid,password=pwd)
                user.save();
                print("USER CREATED")
                return redirect('login')
        else:
            messages.info(request,"PASSWORD NOT MATCHING")
            return redirect('register')


    return render(request,'test.html')
def logout(request):
    auth.logout(request)
    return redirect('login')
