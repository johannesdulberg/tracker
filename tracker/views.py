from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import forms
from .models import Excercise, Set, Training
from django.conf import settings
from django.contrib.auth.decorators import login_required
User = settings.AUTH_USER_MODEL


def index(request):

    return render(request, "tracker/tracking.html")


def record(request):
    if request.user.is_authenticated:

        trainings = Training.objects.filter(
            userTraining=request.user).order_by('Date')
        print(trainings)

        trainingDict = {}
        for i in trainings:
            trainingDict[i] = list(Set.objects.filter(Training=i))

        print("TRAINING DICT", trainingDict)
        return render(request, 'tracker/record.html', {'trainingDict': trainingDict})
    else:
        return render(request, 'tracker/record.html')


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


def createWorkout(request):
    if request.user.is_authenticated:

        if request.method == 'POST':
            # Handle each form submission separately
            if 'exercise_submit' in request.POST:
                exercise_form = forms.CreateExercise(
                    request.POST, request.FILES)
                if exercise_form.is_valid():
                    # save exercise to db
                    instance = exercise_form.save(commit=False)
                    instance.author = request.user
                    instance.save()
                    return redirect('tracker:createWorkout')
            elif 'set_submit' in request.POST:
                set_form = forms.CreateSet(
                    request.user, request.POST, request.FILES)
                if set_form.is_valid():
                    # save set to db
                    instance = set_form.save(commit=False)
                    instance.save()
                    return redirect('tracker:createWorkout')
            elif 'training_submit' in request.POST:
                training_form = forms.CreateTraining(
                    request.POST, request.FILES)
                if training_form.is_valid():
                    # save training to db
                    instance = training_form.save(commit=False)
                    instance.userTraining = request.user
                    instance.save()
                    return redirect('tracker:createWorkout')
        else:
            exercise_form = forms.CreateExercise()
            set_form = forms.CreateSet(request.user)
            training_form = forms.CreateTraining()
        return render(request, 'tracker/createWorkout.html', {
            'exercise_form': exercise_form,
            'set_form': set_form,
            'training_form': training_form,
        })
    else:
        return render(request, 'tracker/createWorkout.html')
