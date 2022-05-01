from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def get_tee_times(request):
  tee_times = [
    {
      'time': '7:00 am',
    },
    {
      'time': '7:10 am',
    },
    {
      'time': '7:20 am',
    },
    {
      'time': '7:30 am',
    },
    {
      'time': '7:40 am',
    },
    {
      'time': '7:50 am',
    },
    {
      'time': '8:00 am',
    },
    {
      'time': '8:10 am',
    },
    {
      'time': '8:20 am',
    },
  ]
  return Response(tee_times) 
