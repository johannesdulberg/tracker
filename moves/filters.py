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


class UserRelatedFilter(django_filters.ChoiceFilter):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        print("USER IS", self.user)

    def filter(self, qs, value):
        if self.user is None or not self.user.is_authenticated:
            if value == 'not_shown' or value == 'shown':
                return qs
            else:  # value == 'only'
                return qs.none()
        if self.user is None:
            return qs
        if value == 'not_shown':
            return qs.exclude(**{self.field_name: self.user})
        elif value == 'shown':
            return qs
        elif value == 'only':
            return qs.filter(**{self.field_name: self.user})
        return qs


class ExerciseFilter(django_filters.FilterSet):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.filters['favorite'] = UserRelatedFilter(choices=(
            ('not_shown', 'Not in Favorites'),
            ('shown', 'All Exercises'),
            ('only', 'Only in Favorites'),
        ), field_name='favorited', user=user)

        self.filters['learned'] = UserRelatedFilter(choices=(
            ('not_shown', 'Not Learned'),
            ('shown', 'All Exercises'),
            ('only', 'Only Learned'),
        ), field_name='learned', user=user)

        self.filters['want_to_learn'] = UserRelatedFilter(choices=(
            ('not_shown', 'Not Display Want To Learn'),
            ('shown', 'All Exercises'),
            ('only', 'Only Want to Learn'),
        ), field_name='want_to_learn', user=user)
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

    favorite = UserRelatedFilter(choices=(
        ('not_shown', 'Not in Favorites'),
        ('shown', 'All Exercises'),
        ('only', 'Only in Favorites'),
    ), field_name='favorited')

    learned = UserRelatedFilter(choices=(
        ('not_shown', 'Not Learned'),
        ('shown', 'All Exercises'),
        ('only', 'Only Learned'),
    ), field_name='learned')

    want_to_learn = UserRelatedFilter(choices=(
        ('not_shown', 'Not Display Want To Learn'),
        ('shown', 'All Exercises'),
        ('only', 'Only Want to Learn'),
    ), field_name='want_to_learn')

    class Meta:
        model = Exercise
        fields = ['difficulty', 'type', "base", "dance",
                  "flows", "washing_machines", "whips", "pops", "counterbalance", "position", "variation",   "entrance_to", "exit_from",  "transition_from", "transition_to", 'favorite', 'learned', 'want_to_learn']
