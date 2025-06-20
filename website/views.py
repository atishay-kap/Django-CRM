from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    
    if request.method != 'POST':
        return render(request , 'home.html' , {})
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request , username = username , password = password)

    if user is not None:
        login(request , user)
        messages.success(request, 'You have been logged in')
    else:
        messages.error(request , 'There was an error logging in, Please try again later...')
    return redirect('home')


def logout_user(request):
    logout(request)
    messages.success(request , "You have been Logged Out Successfully..")
    return redirect('home')

def register_user(request):
    return render(request , 'register.html' , {})