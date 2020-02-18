from datetime import datetime
from django.db import models

class Point(models.Model):
	x = models.FloatField()
	y = models.FloatField()

	class Meta:
		unique_together = ['x', 'y', ]

class Search(models.Model):
	NEAREST = 'N'	
	FURTHEST = 'F'	
	OPERATION_CHOICES = [
		(NEAREST, 'Nearest'),
		(FURTHEST, 'Furthest'),
	]
	timestamp = models.DateTimeField(default=datetime.now, blank=True)
	search_x = models.FloatField()
	search_y = models.FloatField()
	operation = models.CharField(
		max_length=1,
		choices=OPERATION_CHOICES,
		default=NEAREST,
	)
	points = models.PositiveIntegerField()
