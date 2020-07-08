from rest_framework import serializers
from .models import UserTask,  ActivityPeriod

class ActivityPeriodSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = ActivityPeriod
		fields = ('start_time', 'end_time')

class UserTaskSerializer(serializers.HyperlinkedModelSerializer):
	activity_periods = ActivityPeriodSerializer(many=True, source='activityperiod_set', read_only =True)
	class Meta:
		model = UserTask
		fields = ('id', 'real_name', 'tz', 'activity_periods')
		



		