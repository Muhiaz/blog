from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from restaurants.models import Restaurants
from recipies.models import Recipies
from dishes.models import Dishes
from news.models import News


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
    	model = User
    	fields = ["username", "email", "password1", "password2"]

class NewsForm(forms.ModelForm):
	class Meta:
		model= News
		fields= ["title", "image", "description"]
class Addrecipies(forms.ModelForm):
	class Meta:
		model= Recipies
		fields= ["name", "image", "description"]
# 	name =  forms.CharField(
# 		widget=forms.TextInput(
# 			attrs={
# 			"class":"form-control"
# 			}
# 			)
# 		)
# 	image =  forms.CharField(
# 		widget=forms.TextInput(
# 			attrs={
# 			"class":"form-control"
# 			}
# 			)
# 		)
# 	description =  forms.CharField(
# 		widget=forms.Textarea(
# 			attrs={
# 			"class":"form-control"
# 			}
# 			))


class Adddishes(forms.Form):
		
	name= forms.CharField(
			widget=forms.TextInput(
			attrs={
			"class":"form-control"
			}
			)
		)
	image =  forms.CharField(
		widget=forms.TextInput(
			attrs={
			"class":"form-control"
			}
			)
		)
	description =  forms.CharField(
		widget=forms.Textarea(
			attrs={
			"class":"form-control"
			}
			))


class Addrestaurants(forms.ModelForm):
	class Meta:
		model= Restaurants
		fields= ["name", "image", "description","location"]
# 		widget=forms.TextInput(
# 			attrs={
# 			"class":"form-control"
# 			}
# 			)
# 		)
# 	image =  forms.CharField(
# 		widget=forms.TextInput(
# 			attrs={
# 			"class":"form-control"
# 			}
# 			)
# 		)
# 	location =  forms.CharField(
# 		widget=forms.TextInput(
# 			attrs={
# 			"class":"form-control"
# 			}
# 			)
# 		)
# 	description =  forms.CharField(
# 		widget=forms.Textarea(
# 			attrs={
# 			"class":"form-control"
# 			}
# 			))

class Login(forms.Form):
	username =  forms.CharField(
		widget=forms.TextInput(
			attrs={
			"class":"form-control"
			}
			)
		)
	password =  forms.CharField(
		widget=forms.PasswordInput(
			attrs={
			"class":"form-control"
			}
			)
		)
class Registerform(forms.Form):
	username =  forms.CharField(
		widget=forms.TextInput(
			attrs={
			"class":"form-control"
			}
			)
		)
	email =  forms.EmailField(
		widget=forms.TextInput(
			attrs={
			"class":"form-control"
			}
			)
		)
	password =  forms.CharField(
		widget=forms.PasswordInput(
			attrs={
			"class":"form-control"
			}
			)
		)
	confirmpassword =  forms.CharField(
		widget=forms.PasswordInput(
			attrs={
			"class":"form-control"
			}
			)
		)
	
	def clean(self):
		data = self.cleaned_data
		password = self.cleaned_data.get("password")
		confirmpassword = self.cleaned_data.get("confirmpassword")
		if confirmpassword != password:
			raise forms.ValidationError("Passwords must match")
		return data
	user = get_user_model()
	def clean_email(self):
		data = self.cleaned_data
		email = self.cleaned_data.get("email")
		qs = user.objects.filter(email=email)
		if qs.exists() :
			raise forms.ValidationError("Email taken!")
		return data
	
	def clean_username (self):
		global  user
		user = get_user_model()
		data = self.cleaned_data
		username = self.cleaned_data.get("username ")
		qs = user.objects.filter(username =username )
		if qs.exists() :
			raise forms.ValidationError("username  taken!")
		return data
