from django.contrib import admin
from django.urls import path, include
from .views import get_tee_times, update_tee_time

urlpatterns = [
    path('teetimes', get_tee_times, name='getteetimes'),
    path('teetimes/<str:pk>', update_tee_time, name='updateteetime'),
]
