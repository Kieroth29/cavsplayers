from django.db import models

class Player(models.Model):
	
	name = models.CharField(max_length=100)
	number = models.IntegerField()
	main_position = models.CharField(max_length=2)