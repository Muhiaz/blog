from django.db import models

# Create your models here.
class News(models.Model):
	"""docstring for ClassName"""
	title = models.CharField(max_length=120)
	image = models.ImageField(upload_to="news/",blank=True,null=True)
	description = models.TextField()

	
	def __str__(self):
		return self.title


