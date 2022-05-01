from django.contrib import admin
from django.urls import path, include
from .views import get_tee_times

urlpatterns = [
    path('teetimes', get_tee_times, name='getteetimes'),
]
