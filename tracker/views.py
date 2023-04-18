from django.db.models.functions import Coalesce
from django.db.models import Sum, Max
from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import forms
from .models import Excercise, Set, Training
import json
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


def index(request):

    return render(request, "home/home.html")


def chart_data(request):
    if request.user.is_authenticated:
        exercise_id = request.GET.get('exercise_id', None)

        if exercise_id:
            # print(exercise_id)
            exercise = Excercise.objects.get(id=exercise_id)
            sets = Set.objects.filter(
                Excercise=exercise).filter(
                Training__userTraining=request.user).order_by('Training__Date')

        else:
            sets = Set.objects.all().order_by('Training__Date')

        labels = [s.Training.Date for s in sets]
        data = [(s.Reps, s.Weight) for s in sets]

        print("labels", labels, "data", data)

        exercises = Excercise.objects.filter(author=request.user)
        trainDic = {}
        for i in range(len(labels)):
            if labels[i] in trainDic:
                trainDic[labels[i]] += data[i][0]*data[i][1]
            else:
                trainDic[labels[i]] = data[i][0]*data[i][1]
        volumeLable = list(trainDic.keys())
        print("volumeLable", volumeLable)
        volumedata = list(trainDic.values())

        maxSetDic = {}
        for i in range(len(labels)):
            if labels[i] in maxSetDic:
                maxSetDic[labels[i]] = max(
                    data[i][1], maxSetDic[labels[i]])

            else:
                maxSetDic[labels[i]] = data[i][1]

        maxSetLable = list(maxSetDic.keys())
        maxSetData = list(maxSetDic.values())

        oneRepMaxDic = {}
        oneRepMaxDicMax = {}
        for i in range(len(labels)):
            if labels[i] in oneRepMaxDic:
                if data[1][1] > oneRepMaxDic[labels[i]][1]:
                    oneRepMaxDic[labels[i]] = data[i]
                    oneRepMaxDicMax[labels[i]] = data[i][1] * \
                        (36/(37-data[i][0]))
            else:
                oneRepMaxDic[labels[i]] = data[i]
                oneRepMaxDicMax[labels[i]] = data[i][1]*(36/(37-data[i][0]))

        oneRepMaxLable = list(oneRepMaxDicMax.keys())
        oneRepMaxData = list(oneRepMaxDicMax.values())
        for i in maxSetDic:
            maxSetDic
        chart_data = {
            'volumeLable': json.dumps([label.strftime("%Y-%m-%d") for label in volumeLable]),
            'volumeData': json.dumps(volumedata),
            'maxSetLable': json.dumps([label.strftime("%Y-%m-%d") for label in maxSetLable]),
            'maxSetData': json.dumps(maxSetData),
            'oneRepMaxLable': json.dumps([label.strftime("%Y-%m-%d") for label in oneRepMaxLable]),
            'oneRepMaxData': json.dumps(oneRepMaxData),
            'exercises': exercises,
            'selected_exercise': exercise if exercise_id else None
        }

        return render(request, 'tracker/chart.html', chart_data)
    else:
        return render(request, 'tracker/chart.html')
