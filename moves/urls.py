from django.urls import path
from . import views
app_name = "moves"
urlpatterns = [
    path('exercises/', views.exercise_list, name='exercise_list'),
    path('create/', views.createExercise, name='createExercise'),
    path('exercises/<int:exercise_id>/',
         views.exercise_detail, name='exercise_detail'),
    path('add_favorite/<int:exercise_id>/',
         views.add_favorite, name='add_favorite'),
    path('add_learned/<int:exercise_id>/',
         views.add_learned, name='add_learned'),
    path('add_want_to_learn/<int:exercise_id>/',
         views.add_want_to_learn, name='add_want_to_learn'),
]
