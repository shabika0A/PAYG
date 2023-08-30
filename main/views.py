from django.shortcuts import render,redirect
from .forms import RegistrForm
from django.contrib.auth import login,logout,authenticate
from django.shortcuts import render
#from django.contrib.auth.models import User
from main.models import User
# Create your views here.

def home(request):
    user = request.user
    user.reqCount += 1
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

from datetime import date
from rest_framework import permissions, status,serializers 
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CostSerializer  
# from .models import User  # Import your User model
# from rest_framework import  # Create a serializer for the response

class CostAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = self.request.user
        current_month = date.today().month
        
        # Replace 'costperreq' with your actual cost per request value


        # Calculate the cost for the current month
        # cost = costperreq * user.reqCount

        data = {
            
            "username": user.username,
            "current_month": current_month,
            "request_count": user.reqCount,
            "cost": user.totalCost
        }

        serializer = CostSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)
