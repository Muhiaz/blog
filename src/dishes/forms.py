from dishes.models import Dishes
from django import forms

class Adddishes(forms.ModelForm):
	class Meta:
		model= Dishes
		fields= ["name", "image", "description"]