
from rest_framework import  serializers
from .models import activity_period
from accounts.models import User

# UserSerializer is a Model Based Nested Serializer, Nested because for every user object it calls for ActivityPeriodSerializer.
class ActivityPeriodSerializer(serializers.ModelSerializer):
    start_time = serializers.DateTimeField(format='%b %e %Y %l:%M %p')
    end_time = serializers.DateTimeField(format='%b %e %Y %l:%M %p')

    class Meta:
        model = activity_period
        fields = ['start_time', 'end_time']

# ActivityPeriodSerializer is a Model Based Serializer. Format of DateTimeField is explicity defined in the serializer
class UserSerializer(serializers.ModelSerializer):
    activity_periods = ActivityPeriodSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'real_name', 'tz', 'activity_periods']

