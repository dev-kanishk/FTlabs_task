
from rest_framework import  serializers
from .models import activity_period
from accounts.models import User


class ActivityPeriodSerializer(serializers.ModelSerializer):
    start_time = serializers.DateTimeField(format='%b %e %Y %l:%M %p')
    end_time = serializers.DateTimeField(format='%b %e %Y %l:%M %p')

    class Meta:
        model = activity_period
        fields = ['start_time', 'end_time']

class UserSerializer(serializers.ModelSerializer):
    activity_periods = ActivityPeriodSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'real_name', 'tz', 'activity_periods']

