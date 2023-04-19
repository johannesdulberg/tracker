from django.http import HttpResponse
from django.shortcuts import render, redirect


def index(request):

    return render(request, "home/home.html")


def impressum(request):

    return render(request, "home/impressum.html")
