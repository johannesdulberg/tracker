import django_filters
from .models import Exercise


class ThreeOptionChoiceFilter(django_filters.ChoiceFilter):
    def filter(self, qs, value):
        if value == 'not_shown':
            return qs.exclude(**{self.field_name: True})
        elif value == 'shown':
            return qs
        elif value == 'only':
            return qs.filter(**{self.field_name: True})
        return qs


class ExerciseFilter(django_filters.FilterSet):
    difficulty = django_filters.ChoiceFilter(
        choices=Exercise.DIFFICULTY_CHOICES)
    importance = django_filters.ChoiceFilter(
        choices=Exercise.IMPORTANCE_CHOICES)
    base = django_filters.ChoiceFilter(
        choices=Exercise.BASE_CHOICES)
    dance = ThreeOptionChoiceFilter(choices=(
        ('not_shown', 'No Dancemoves'),
        ('shown', 'Also Dancemoves'),
        ('only', 'Just Dancemoves'),
    ))
    washing_machines = ThreeOptionChoiceFilter(choices=(
        ('not_shown', 'No Washing Machines'),
        ('shown', 'Also Washing Machines'),
        ('only', 'Just Washing Machines'),
    ))
    flows = ThreeOptionChoiceFilter(choices=(
        ('not_shown', 'No Flows'),
        ('shown', 'Also Flows'),
        ('only', 'Just Flows'),
    ))
    whips = ThreeOptionChoiceFilter(choices=(
        ('not_shown', 'No Whips'),
        ('shown', 'Also Whips'),
        ('only', 'Just Whips'),
    ))
    pops = ThreeOptionChoiceFilter(choices=(
        ('not_shown', 'No Pops'),
        ('shown', 'Also Pops'),
        ('only', 'Just Pops'),
    ))

    class Meta:
        model = Exercise
        fields = ['difficulty', 'importance', "base", "dance",
                  "flows", "washing_machines", "whips", "pops"]
