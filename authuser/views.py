

from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import login, logout

from django.contrib.auth.decorators import login_required


def signup_view(request):
    print("YOUR METHOD", request.method)
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('authuser:login')

    else:
        print("GET")
        form = CustomUserCreationForm()
    return render(request, 'authuser/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log the user in
            # return redirect('articles:list')
            user = form.get_user()
            login(request, user)
            return redirect('moves:exercise_list')
    else:
        form = AuthenticationForm()
    return render(request, 'authuser/login.html', {'form': form})


@login_required
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')
    return render(request, 'authuser/logout.html')
