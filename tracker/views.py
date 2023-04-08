from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import forms
from .models import Excercise, Set, Training
from django.conf import settings
User = settings.AUTH_USER_MODEL


def index(request):

    return render(request, "tracker/tracking.html")


def record(request):

    trainings = Training.objects.filter(
        userTraining=request.user).order_by('Date')
    print(trainings)

    trainingDict = {}
    for i in trainings:
        trainingDict[i] = list(Set.objects.filter(Training=i))

    print("TRAINING DICT", trainingDict)
    return render(request, 'tracker/record.html', {'trainingDict': trainingDict})


def createExercise(request):
    print(User)
    if request.method == 'POST':
        form = forms.CreateExercise(request.POST, request.FILES)
        if form.is_valid():
            # save article to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('tracker:createExercise')
    else:
        form = forms.CreateExercise()
    return render(request, "tracker/createExercise.html", {'form': form})


def createSet(request):
    if request.method == 'POST':
        form = forms.CreateSet(request.user, request.POST, request.FILES)
        if form.is_valid():
            # save article to db
            print("SAVED")
            instance = form.save(commit=False)
            instance.save()

            return redirect('tracker:createSet')
    else:
        form = forms.CreateSet(request.user)
    return render(request, "tracker/createSet.html", {'form': form})


def createTraining(request):
    if request.method == 'POST':
        form = forms.CreateTraining(request.POST, request.FILES)
        if form.is_valid():
            # save article to db
            print("SAVED")
            instance = form.save(commit=False)
            instance.userTraining = request.user
            instance.save()
            return redirect('tracker:createTraining')
    else:
        form = forms.CreateTraining()
    return render(request, "tracker/createTraining.html", {'form': form})
