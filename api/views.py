from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import TeeTimesSerializer
from .models import TeeTimes
# from rest_framework import filters

@api_view(['GET'])
def get_tee_times(request):
  all_tee_times = TeeTimes.objects.all()
  serialized = TeeTimesSerializer(all_tee_times, many=True)
  # print(serialized)
  # print(type(serialized))

  return Response(serialized.data) 


# class GetAllTeeTimes(filters.SearchFilter):
#   queryset = TeeTimes.objects.all()
#   serializer_class = TeeTimesSerializer
#   filter_backends = [filter.OrderingFilter]
#   ordering_fields = ['date','time']



@api_view(['PUT'])
def update_tee_time(request, pk):
  # print("in PUT function")
  tee_time = TeeTimes.objects.get(id=pk)
  serialized = TeeTimesSerializer(instance=tee_time, data=request.data)
  if serialized.is_valid():
    serialized.save()
  else:
    print("something went wrong with trying to save. serializer not valid.")
  # print(type(serialized))

  return Response(serialized.data) 