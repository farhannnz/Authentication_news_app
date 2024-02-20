from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.shortcuts import HttpResponse, render , redirect
from userapp.models import Blog


# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request, 'index.html') 

def log_in(request):
   if request.method== 'POST':
     username = request.POST.get('username')
     password = request.POST.get('password')
     user=authenticate(username=username, password=password)
     if user is not None:
       login(request,user)
       return redirect ('/')
     else:
       return redirect ('/login')
   return render(request,'signin.html')

def log_out(request):
  logout(request)
  return redirect ('/login')

def sign_up(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword') 
        if password == cpassword:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
        return redirect('/login')  # Fixed closing single quote
    return render(request, 'signup.html')

def blog(request):
    if request.user.is_anonymous:
        return redirect('/login')
    news = Blog.objects.all()
    
    return render(request,'blog.html',{'news':news})



