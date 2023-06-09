from django.urls import path

from . import views
app_name = "tracker"
urlpatterns = [
    path('', views.index, name='index'),
    path('record/', views.record, name='record'),
    path('createWorkout/', views.createWorkout, name='createWorkout'),
    path('metrics/', views.chart_data, name="metrics"),
]
