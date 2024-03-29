from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name ="home"),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('signout', views.signout, name="signout"), 
    path('about', views.about, name="about"), 
    path('profile', views.profile, name="profile"),   
    path('clocked', views.clocked, name="clocked"),
    path('clockview', views.clockview, name="clockview"), 

]