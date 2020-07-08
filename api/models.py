from django.db import models

# Create your models here.
class UserTask(models.Model):
	real_name = models.CharField(max_length = 120)
	tz = models.CharField(max_length=120)

	def __str__(self):
		return (self.real_name)

class ActivityPeriod(models.Model):
	user = models.ForeignKey(UserTask, on_delete = models.CASCADE)
	start_time = models.DateTimeField()
	end_time = models.DateTimeField()
