from django.shortcuts import render,redirect
from .forms import RegistrForm
from django.contrib.auth import login,logout,authenticate
from django.shortcuts import render
#from django.contrib.auth.models import User
from main.models import User
# Create your views here.

def home(request):
    user = request.user
    user.reqcount += 1
    user.save()
    return render(request,'main/home.html')

def sign_up(request):
    if request.method =='POST':
        form=RegistrForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('/home')
    else:
        form=RegistrForm()
    
    return render(request,'registration/sign_up.html',{"form":form})

def list_users(request):
    all_users = User.objects.all()
    return render(request, 'main/user_list.html', {'users': all_users})
