from django.shortcuts import render, get_object_or_404
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


def exercise_detail(request, exercise_id):
    exercise = get_object_or_404(Exercise, id=exercise_id)

    variations = Exercise.objects.filter(variation=exercise)
    entrances = Exercise.objects.filter(entrance_to=exercise)
    exits = Exercise.objects.filter(exit_from=exercise)
    transitions_from = Exercise.objects.filter(transition_from=exercise)
    transitions_to = Exercise.objects.filter(transition_to=exercise)

    context = {
        'exercise': exercise,
        'variations': variations,
        'entrances': entrances,
        'exits': exits,
        'transitions_from': transitions_from,
        'transitions_to': transitions_to,
    }

    return render(request, 'moves/exercise_detail.html', context)
