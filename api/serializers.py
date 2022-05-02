from rest_framework import serializers
from .models import TeeTimes

class TeeTimesSerializer(serializers.ModelSerializer):
  class Meta:
    model = TeeTimes
    fields = ("id", "date","time","is_reserved","player_1_name","player_1_is_checkedin")