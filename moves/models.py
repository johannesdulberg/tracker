from django.db import models


class Exercise(models.Model):
    DIFFICULTY_CHOICES = (
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    )
    BASE_CHOICES = (
        ('lbase', 'L-Base'),
        ('standing', 'Standing'),
    )
    IMPORTANCE_CHOICES = (
        ('important', 'Important'),
        ('variation', 'Variation'),
        ('interesting', 'Interesting'),
        ('whanky', "whanky")
    )

    name = models.CharField(max_length=255)
    difficulty = models.CharField(max_length=100, choices=DIFFICULTY_CHOICES)
    base = models.CharField(max_length=100, choices=BASE_CHOICES)
    importance = models.CharField(max_length=100, choices=IMPORTANCE_CHOICES)
    dance = models.BooleanField(default=False)
    washing_machines = models.BooleanField(default=False)
    flows = models.BooleanField(default=False)
    whips = models.BooleanField(default=False)
    pops = models.BooleanField(default=False)
    legit = models.BooleanField(default=False)
    video_url = models.URLField()

    def __str__(self):
        return self.name
