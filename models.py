from django.db import models
from datetime import datetime
# Create your models here.
class Vehicles(models.Model):
	year = models.PositiveSmallIntegerField()
	make = models.CharField(max_length=30)
	model = models.CharField(max_length=30)
	created_at = models.DateTimeField(default=datetime.now, blank=True)
	def __str__(self):
		return str(self.year) + " " + self.make + " " + self.model
	class Meta:
		verbose_name_plural = "Vehicles"