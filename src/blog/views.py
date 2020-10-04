from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from dishes.forms import Adddishes
from .forms import NewsForm,Addrecipies,Addrestaurants,Login,RegisterForm
from dishes.models import  Dishes
from news.models import  News
from django.contrib.auth.models import User
from restaurants.models import Restaurants
from recipies.models import Recipies

def home_page(request):
	dishes = Dishes.objects.all().order_by('-id')[:4]
	restaurants = Restaurants.objects.all()[:4]
	recipies = Recipies.objects.all().order_by('-id')[:4]
	news = News.objects.all().order_by('-id')[:4]
	context  = {
	"form": dishes,
	"news": news,
	"restaurants":restaurants,
	"recipies":recipies,
	}
	return render(request,"home_page.html",context);
def alldishes(request):
		dishes = Dishes.objects.all()
		context  = {
		"form": dishes,
		}
		return render(request,"alldishes.html",context);
		
def allrestaurants(request):
		restaurants = Restaurants.objects.all()
		context  = {
		"restaurants":restaurants,
		}
		return render(request,"allrestaurants.html",context);
def contact(request):
		restaurants = Restaurants.objects.all()
		context  = {
		"restaurants":restaurants,
		}
		return render(request,"contact.html",context);
def allrecipies(request):
		recipies = Recipies.objects.all()
		context  = {
		"recipies":recipies,
		}
		return render(request,"allrecipies.html",context);
def detail_view(request,pk=None):
	dishes = Dishes.objects.get(pk=pk)
	context  = {
	"form": dishes
	}
	return render(request,"detail_view.html",context);

def dish(request,pk=None):
	dishes = Dishes.objects.get(pk=pk)
	context  = {
	"form": dishes
	}
	return render(request,"dishdetail_view.html",context);
def recipie(request,pk=None):
	dishes = Recipies.objects.get(pk=pk)
	context  = {
	"form": dishes
	}
	return render(request,"recipiedetail_view.html",context);
def restaurant(request,pk=None):
	dishes = Restaurants.objects.get(pk=pk)
	context  = {
	"form": dishes
	}
	return render(request,"restaurantdetail_view.html",context);
def news(request,pk=None):
	dishes = News.objects.get(pk=pk)
	context  = {
	"form": dishes
	}
	return render(request,"newsdetail_view.html",context);
def allnews(request):
	dishes = News.objects.all()
	context  = {
	"form": dishes
	}
	return render(request,"allnews.html",context);

@csrf_exempt
def login_page(request):
	global Login
	loginform = Login(request.POST or None)
	context  = {
	"form": loginform
	}
	print(request.user.is_authenticated)
	if request.method == 'POST':
		if loginform.is_valid():
			print(loginform.cleaned_data)
		print(request.POST)
		username = loginform.cleaned_data.get("username")
		password = loginform.cleaned_data.get("password")
		user = authenticate(request,username=username ,password=password)
		if user is not None:
			login(request, user)
			print(request.user.is_authenticated)
			context['form'] = Login()
		else:
			print('error')
	return render(request,"auth/login_page.html",context);


@csrf_exempt
def register_page(request):
	global Registerform
	registerform = RegisterForm(request.POST or None)
	context  = {
	"form": registerform
	}
	print(request.user.is_authenticated)
	if request.method == "POST":
		if registerform.is_valid():
		    registerform.save()
	return render(request,"auth/register_page.html",context);
@csrf_exempt
def addrecipies(request):
	global addrecipies
	addrecipies = Addrecipies(request.POST, request.FILES or None)
	if addrecipies.is_valid():
		addrecipies.save()
		print(addrecipies.cleaned_data)
		return redirect('/allrecipies')
	context  = {
	"form": addrecipies
	}
	print(request.POST)
	return render(request,"addrecipies.html",context);
@csrf_exempt
def adddishes(request):
	global adddishes
	
	adddishes = Adddishes()
	if request.method=='POST':
		adddishes = Adddishes(request.POST, request.FILES or None)
		if adddishes.is_valid():
			adddishes.save()
			print(adddishes.cleaned_data)
			return redirect('/alldishes')
	context  = {
	"form": adddishes
	}
	print(request.POST)
	return render(request,"adddishes.html",context);
@csrf_exempt
def addnews(request):
	global addishes
	
	addishes = NewsForm()
	if request.method=='POST':
		addishes = NewsForm(request.POST, request.FILES or None)
		if addishes.is_valid():
			addishes.save()
			print(addishes.cleaned_data)
			return redirect('/allnews')
	context  = {
	"form": addishes
	}
	print(request.POST)
	return render(request,"addnews.html",context);
@csrf_exempt
def addrestaurants(request):
	global addrestaurants
	addrestaurants = Addrestaurants(request.POST, request.FILES or None)
	if addrestaurants.is_valid():
		addrestaurants.save()
		print(addrestaurants.cleaned_data)
		return redirect('/allrestaurants')
	context  = {
	"form": addrestaurants
	}
	return render(request,"addrestaurants.html",context);