from django.contrib import admin
from django.urls import include, path
from . import views
app_name = "authuser"
urlpatterns = [
    path('signup/', views.signup_view, name="signup"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('profile/', views.profile, name='profile'),
]
