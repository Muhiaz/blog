from django.db import models
import os
import random
def get_filename_ext(filepath):
	base_name = os.path.basename(filepath)
	name, ext = os.path.splitext(base_name)
	return name, ext
def get_filename(instance,filename):
	new_filename = random.randint(1,3000000)
	name, ext = get_filename_ext(filename)
	final_filename =  f'{new_filename}{ext}'
	return f"restaurants/{new_filename}/{final_filename}"
# Create your models here.
class Restaurants(models.Model):
	name = models.CharField(max_length=120)
	image = models.ImageField(upload_to='restaurants/',blank=True,null=True)
	location = models.CharField(max_length=120)
	description = models.TextField()

	def __str__(self):
		return self.name
