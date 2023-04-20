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
    type = django_filters.ChoiceFilter(
        choices=Exercise.TYPE_CHOICES)
    base = django_filters.ChoiceFilter(
        choices=Exercise.BASE_CHOICES)
    dance = ThreeOptionChoiceFilter(choices=(
        ('not_shown', 'No Dancemoves'),
        ('shown', 'Also Dancemoves'),
        ('only', 'Only Dancemoves'),
    ))
    washing_machines = ThreeOptionChoiceFilter(choices=(
        ('not_shown', 'No Washing Machines'),
        ('shown', 'Also Washing Machines'),
        ('only', 'Only Washing Machines'),
    ))
    flows = ThreeOptionChoiceFilter(choices=(
        ('not_shown', 'No Flows'),
        ('shown', 'Also Flows'),
        ('only', 'Only Flows'),
    ))
    whips = ThreeOptionChoiceFilter(choices=(
        ('not_shown', 'No Whips'),
        ('shown', 'Also Whips'),
        ('only', 'Only Whips'),
    ))
    pops = ThreeOptionChoiceFilter(choices=(
        ('not_shown', 'No Pops'),
        ('shown', 'Also Pops'),
        ('only', 'Only Pops'),
    ))
    counterbalance = ThreeOptionChoiceFilter(choices=(
        ('not_shown', 'No Counterbalance'),
        ('shown', 'Also Counterbalance'),
        ('only', 'Only Counterbalance'),
    ))
    position = ThreeOptionChoiceFilter(choices=(
        ('not_shown', 'No Positions'),
        ('shown', 'Also Positions'),
        ('only', 'Only Positions'),
    ))

    class Meta:
        model = Exercise
        fields = ['difficulty', 'type', "base", "dance",
                  "flows", "washing_machines", "whips", "pops", "counterbalance", "position", "variation",   "entrance_to", "exit_from",  "transition_from", "transition_to"]
