from django.db import models

def get_filename_ext(filepath):
	base_name = os.path.basename(filepath)
	name, ext = os.path.splitext(base_name)
	return name, ext
def get_filename(instance,filename):
	new_filename = random.randint(1,3000000)
	name, ext = get_filename_ext(filename)
	final_filename =  f'{new_filename}{ext}'
	return f"recipies/{new_filename}/{final_filename}"
# Create your models here.
class Recipies(models.Model):
	name = models.CharField(max_length=120)
	image = models.ImageField(upload_to='recipies/',blank=True,null=True)
	description = models.TextField()

	def __str__(self):
		return self.name



	


