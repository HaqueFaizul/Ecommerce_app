from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def loadregister(request):
    return render(request,"register.html")

def loadlogin(request):
    return render(request,'login.html')

def Register(request):
    if request.method=='POST':
        vfname=request.POST.get('fname')
        vlname=request.POST.get('lname')
        vuname=request.POST.get('uname')
        vemail=request.POST.get('email')
        vpasswd=request.POST.get('passwd')
        vrpasswd=request.POST.get('rpasswd')
        #return HttpResponse(vemail)
        if vpasswd == vrpasswd:
            if User.objects.filter(username=vuname).exists():
                messages.success(request,'Username already exist')
                return redirect('/')
            elif User.objects.filter(email=vemail).exists():
                return redirect('/')
            else:
                newuser=User.objects.create_user(first_name=vfname,last_name=vlname,username=vuname,email=vemail,password=vpasswd)
                newuser.save()
                return redirect('/account/login')
        else:
            return redirect('/')

def Login(request):
    if request.method == 'POST':
        vuname=request.POST.get('uname')
        vpasswd = request.POST.get('passwd')

        newuser = auth.authenticate(username=vuname, password=vpasswd)
        if newuser is not None:
            auth.login(request, newuser)
            #return redirect('/account/deshbord')
            return render(request, 'dashbord.html')
        else:
            return render(request, 'register.html')
            messages.success(request, "Invalid credentials")

@login_required(login_url='login')
def Logout(request):
    auth.logout(request)
    messages.success(request,"Successfully Logged out")
    return redirect('/account/login')

@login_required(login_url='login')
def Dashbord(request):
    return render(request,'dashbord.html')

'''Steps to push our project to git hub
1. Check the status of git
    git status
2. Track all files before we push it to online repository
    git add -A
3. Make commit of all tracked file
    git commit -m "Commited message"
4. push your commited file to online repository
    git push -u origin main
5. Now your file is successfully pushed to online repository
    go to you github account and check all files has been pushed successfully'''




