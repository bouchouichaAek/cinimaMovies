from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, logout 
from django.contrib.auth import login as Login  
from .forms import ReviewerCreationForm
# Create your views here.

def Regitraion(request):

    form = ReviewerCreationForm()
    if request.method == 'POST':
       form = ReviewerCreationForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('Home') 
    context = {
        'Reviewer' : form,
    }
    return render(request,"registration/registration.html",context)




def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')    
        User = authenticate(request,username = username,password = password)
        if User is not None:
            Login(request,User)
            return redirect('Home')
        else:
            messages.info(request,"username or password incorect")

    return render(request,"registration/login.html")


def logoutuser(request):
    logout(request)
    return redirect('Home')