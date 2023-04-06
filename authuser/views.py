

from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm


def signup_view(request):
    print("YOUR METHOD", request.method)
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #  log the user in
            print("POST SAVED")

    else:
        print("GET")
        form = UserCreationForm()
    return render(request, 'authuser/signup.html', {'form': form})
