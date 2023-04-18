from django.db import models
from django.conf import settings
import datetime
User = settings.AUTH_USER_MODEL


class Excercise(models.Model):
    #user = models.ManyToOneField(User, null=True, on_delete=models.CASCADE)
    author = models.ForeignKey(User, default=User, on_delete=models.CASCADE)
    Excercise = models.TextField()

    def __str__(self):
        return str(self.Excercise)


class Training(models.Model):
    userTraining = models.ForeignKey(
        User, default=None, on_delete=models.CASCADE, null=True)
    Date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return str(self.Date)


class Set(models.Model):
    #user = models.ManyToOneField(User, null=True, on_delete=models.CASCADE)
    Excercise = models.ForeignKey(
        Excercise, default=None, on_delete=models.CASCADE)
    Training = models.ForeignKey(
        Training, default=None, on_delete=models.CASCADE)
    Weight = models.IntegerField()
    Reps = models.IntegerField()

    def __str__(self):
        return str(self.Excercise)+str(self.Training)
