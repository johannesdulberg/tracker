from django import forms
from . import models
from .models import Exercise
import datetime


class CreateExercise(forms.ModelForm):

    class Meta:
        model = models.Exercise
        fields = ["name", "difficulty", "base", "type", "dance",
                  "washing_machines", "flows", "whips", "pops", "counterbalance", "position", "video_url", "variation", "entrance_from", "entrance_to", "exit_from", "exit_to", "transition_from", "transition_to"]


class FavoriteForm(forms.Form):
    exercise_id = forms.IntegerField(widget=forms.HiddenInput())
