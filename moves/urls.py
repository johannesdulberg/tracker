from django.urls import path
from . import views
app_name = "moves"
urlpatterns = [
    path('exercises/', views.exercise_list, name='exercise_list'),
    path('create/', views.createExercise, name='createExercise'),
    path('exercises/<int:exercise_id>/',
         views.exercise_detail, name='exercise_detail'),
]
