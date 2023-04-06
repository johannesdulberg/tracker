from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL


class Excercise(models.Model):
    #user = models.ManyToOneField(User, null=True, on_delete=models.CASCADE)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    Excercise = models.TextField()

    def __str__(self):
        return str(self.Excercise)


class Unit(models.Model):
    #user = models.ManyToOneField(User, null=True, on_delete=models.CASCADE)
    Excercise = models.ForeignKey(
        Excercise, default=None, on_delete=models.CASCADE)
    Date = models.DateField()

    def __str__(self):
        return str(self.Excercise)+" "+str(self.Date)


class Set(models.Model):
    #user = models.ManyToOneField(User, null=True, on_delete=models.CASCADE)
    Set = models.ForeignKey(
        Unit, default=None, on_delete=models.CASCADE)
    Weight = models.IntegerField()
    Reps = models.IntegerField()

    def __str__(self):
        return str(self.Set)
