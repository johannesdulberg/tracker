from django.urls import path

from . import views
app_name = "tracker"
urlpatterns = [
    path('', views.index, name='index'),
    path('createExercise/', views.createExercise, name='createExercise'),
    path('createSet/', views.createSet, name='createSet'),
    path('createTraining/', views.createTraining, name='createTraining'),
    path('record/', views.record, name='record'),
    path('createWorkout/', views.createWorkout, name='createWorkout'),
    path('metrics/', views.chart_data, name="metrics"),
]
