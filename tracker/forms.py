from django import forms
from . import models
from .models import Excercise, Training
import datetime


class CreateTraining(forms.ModelForm):

    class Meta:
        model = models.Training
        fields = ["Date"]


class CreateSet(forms.ModelForm):

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Training'].queryset = Training.objects.filter(
            userTraining=user)
        self.fields['Excercise'].queryset = Excercise.objects.filter(
            author=user)

    class Meta:
        model = models.Set
        fields = ["Excercise", "Weight", "Reps", "Training"]


class CreateExercise(forms.ModelForm):

    class Meta:
        model = models.Excercise
        fields = ["Excercise"]
