from django.shortcuts import render
from rest_framework import generics
from .serializers import UserTaskSerializer, ActivityPeriodSerializer
from .models import UserTask, ActivityPeriod
from rest_framework.response import Response


class CreateView(generics.ListAPIView):
	queryset = UserTask.objects.all()
	serializer_class = UserTaskSerializer


	def list(self, request):     
		queryset = self.get_queryset()    
		serializer = UserTaskSerializer(queryset, many=True)
		context = {
			"ok" : True,
			"members" : serializer.data,
		}  
		return Response(context)

class ActivityPeriodCreateView(generics.ListAPIView):
	queryset = ActivityPeriod.objects.all()
	serializer_class = ActivityPeriodSerializer

	#def perform_create(self, serializer):
	#	serializer.save()