from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Date(models.Model):
	date = models.DateField()

	def __str__(self):
		return f"{self.date}"

class Timestamp(models.Model):
	date = models.ForeignKey(Date, on_delete = models.CASCADE)
	icon = models.CharField(max_length = 255)
	color = models.CharField(max_length = 255)

	def __str__(self):
		return f"{self.date} - {self.icon} - {self.color}"

class Panel(models.Model):
	timestamp = models.ForeignKey(Timestamp, on_delete = models.CASCADE)
	title = models.CharField(max_length = 255)
	description = models.TextField()

	def __str__(self):
		return f"{self.title}"