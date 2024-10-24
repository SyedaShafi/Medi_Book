from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_staff:
                login(request, user)
                messages.success(request, 'Login Successful!')
                return redirect('home-view')
            else:
                messages.warning(request, 'You are not an admin!')
                return redirect('login-view')
        else:
            messages.warning(request, 'Password or username does not match!')
            return redirect('login-view')
        
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login-view')