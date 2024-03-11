
from django.shortcuts import render

from django.contrib.auth.models import User

from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .forms import UserEditForm
# Create your views here.
@csrf_exempt
def User_login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            print("user abc")
            messages.success(request, "welcome {username} to movie project.com ".format(username=username))
            return redirect('/')
        else:
            messages.error(request,"invaild credantialis please check you username and password")
            print("user cdf")
            return redirect('/')

    # return render(request,'login.html')

def User_register(request):
    if request.method=='POST':
        user=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        password=request.POST['password']

        print("this reached")
        # if password==conpass:
        if User.objects.filter(username=user).exists():
            messages.info(request,"username taken")
            print("user")
            return redirect('User_register')
        else:
            us1=User.objects.create_user(username=user,password=password,first_name=fname,last_name=lname,email=email)
            print("lll1")
            us1.save()

            print("created sucess")
            return redirect('/')
        # else:
        #     messages.info(request,"password dont match ")
        #     return redirect('register')
    else:
        # return redirect('fun1')
        pass
    return render(request,"signup.html")
def User_logout(request):
    print("logout started")
    auth.logout(request)
    return redirect("/")

@login_required
def edit_user(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)
        print(form,form.is_valid())
        # print(form.user,"khjbkj")
        if form.is_valid():
            form.save()
            return redirect('/')  # Redirect to profile page after successful update
    else:
        form = UserEditForm(instance=request.user)  # Populate form with current user details
    return render(request, 'profile.html', {'form': form})
