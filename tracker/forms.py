from django import forms
from . import models


class CreateUnit(forms.ModelForm):
    class Meta:
        model = models.Unit
        fields = ["Exercise", "Date"]
