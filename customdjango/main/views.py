from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .models import *
from django.contrib import messages
from django.shortcuts import get_object_or_404
# Create your views here.

def home(request):
    return render(request, 'home.html')

def login_attempts(request):
        
    if request.method == 'POST':    
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user_obj = User.objects.filter(email=email).first()
        
        if user_obj is None:
            messages.error(request, 'User Not Found')
            return redirect('signin')
        
               
        user = authenticate(email=email, password=password)
        
        if user is None:
            messages.error(request, 'Wrong Password')
            return redirect('signin')
        
        login(request, user)
        return redirect('/')
                
    return render(request, 'login.html')


def register_attempts(request):    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        image  = request.POST.get('image')
        
        try:
            if User.objects.filter(email=email).first():
                messages.error(request, 'Email Address already Exists')
                return redirect('signup')
            user_obj = User(name=name, image=image, email=email)
            user_obj.set_password(password)
            user_obj.save()
        except Exception as e:
            print(e)
        
    return render(request, 'registrations.html')



@csrf_exempt
def logout_view(request):
    if(request.user.is_authenticated is False):
        return redirect("signin")
    logout(request)
    return redirect('signin')


def profiles(request, pk=None):
    if pk:
        user = get_object_or_404(User, pk=pk)
    else:
        user = request.user
    return render(request, 'profiles.html', {'user': user})