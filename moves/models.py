from django.db import models


# class Transition(models.Model):
#    from_position = models.ForeignKey("Exercise", related_name='from_transitions',
#                                      on_delete=models.CASCADE, limit_choices_to={'position': True})
#    to_position = models.ForeignKey('Exercise', related_name='to_transitions',
#                                    on_delete=models.CASCADE, limit_choices_to={'position': True})
#
#    def __str__(self):
#        return f'{self.from_position} -> {self.to_position}'


class Exercise(models.Model):
    DIFFICULTY_CHOICES = (
        ('easy', 'Easy'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('expert', 'Expert'),
    )
    BASE_CHOICES = (
        ('lbase', 'L-Base'),
        ('standing', 'Standing'),
    )
    TYPE_CHOICES = (
        ('essential', 'Essential'),
        ('not_essential', 'Not Essential'),
    )

    name = models.CharField(max_length=255)
    difficulty = models.CharField(max_length=100, choices=DIFFICULTY_CHOICES)
    base = models.CharField(max_length=100, choices=BASE_CHOICES)
    type = models.CharField(max_length=100, choices=TYPE_CHOICES)

    dance = models.BooleanField(default=False)
    washing_machines = models.BooleanField(default=False)
    flows = models.BooleanField(default=False)
    whips = models.BooleanField(default=False)
    pops = models.BooleanField(default=False)
    counterbalance = models.BooleanField(default=False)
    position = models.BooleanField(default=False)

    variation = models.ForeignKey('self', null=True, blank=True, related_name='variations',
                                  on_delete=models.CASCADE, limit_choices_to={'position': True})

    # entrance = models.ForeignKey(Transition, null=True, blank=True,
    #                             related_name='exercise_entrances', on_delete=models.SET_NULL)
    # exit = models.ForeignKey(Transition, null=True, blank=True,
    #                         related_name='exercise_exits', on_delete=models.SET_NULL)
    entrance_from = models.ForeignKey('self', null=True, blank=True, related_name='entrance_from_exercises',
                                      on_delete=models.SET_NULL, limit_choices_to={'position': True})
    entrance_to = models.ForeignKey('self', null=True, blank=True, related_name='entrance_to_exercises',
                                    on_delete=models.SET_NULL, limit_choices_to={'position': True})
    exit_from = models.ForeignKey('self', null=True, blank=True, related_name='exit_from_exercises',
                                  on_delete=models.SET_NULL, limit_choices_to={'position': True})
    exit_to = models.ForeignKey('self', null=True, blank=True, related_name='exit_to_exercises',
                                on_delete=models.SET_NULL, limit_choices_to={'position': True})
    transition_from = models.ForeignKey('self', null=True, blank=True, related_name='transition_from_exercises',
                                        on_delete=models.SET_NULL, limit_choices_to={'position': True})
    transition_to = models.ForeignKey('self', null=True, blank=True, related_name='transition_to_exercises',
                                      on_delete=models.SET_NULL, limit_choices_to={'position': True})

    legit = models.BooleanField(default=False)
    video_url = models.URLField()

    def __str__(self):
        return self.name


# class Transition(models.Model):
#    from_position = models.ForeignKey(
#        Exercise, related_name='from_transitions', on_delete=models.CASCADE, limit_choices_to={'position': True})
#    to_position = models.ForeignKey(Exercise, related_name='to_transitions',
#                                    on_delete=models.CASCADE, limit_choices_to={'position': True})
#
#    def __str__(self):
#        return f'{self.from_position} -> {self.to_position}'
