from django.db import models

class Calculator(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField()
	#optional thumbnail might delete
	thumb = models.ImageField(default='default.png', blank = True)

	def __str__(self):
		return self.title