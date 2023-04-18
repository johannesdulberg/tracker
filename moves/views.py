from django.shortcuts import render
from .models import Exercise
from .filters import ExerciseFilter
from django.shortcuts import render, redirect
from . import forms
from .models import Exercise
import json
from django.conf import settings
from django.contrib.auth.decorators import login_required
User = settings.AUTH_USER_MODEL


def exercise_list(request):
    exercise_filter = ExerciseFilter(
        request.GET, queryset=Exercise.objects.filter(legit=True))
    return render(request, 'moves/exercise_list.html', {'filter': exercise_filter})


def createExercise(request):
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
                    return redirect('moves:createExercise')

        else:
            exercise_form = forms.CreateExercise()
        return render(request, "moves/createExercise.html", {
            'exercise_form': exercise_form,
        })
    else:
        return render(request, "moves/createExercise.html")
