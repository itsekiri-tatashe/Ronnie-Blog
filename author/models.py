from datetime import datetime

from django.db import models

# Create your models here.
class Author(models.Model):
	first_name = models.CharField(max_length=200,default="Oghenerhona")
	last_name = models.CharField(max_length=200,default="Ideh")
	snap = models.ImageField(upload_to='data/%Y/%m/%d/',blank =True)
	description = models.TextField(blank=True)
	phone = models.CharField(max_length=20)
	email = models.CharField(max_length=50)
	instagram = models.CharField(max_length=50,blank=True)
	date_joined = models.DateTimeField(default=datetime.now, blank=True)
	slug = models.SlugField(max_length=50,default="oghenerhona-ideh")
	value_1 = models.CharField(max_length=50,default="Journalist")
	value_2 = models.CharField(max_length=50,default="Beautiful")
	
	def __str__(self):
		return self.first_name