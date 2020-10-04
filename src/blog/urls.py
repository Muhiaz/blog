"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import allnews,news,addnews,dish,restaurant,recipie,contact,alldishes,allrestaurants,allrecipies,home_page,detail_view,register_page,addrecipies,adddishes,addrestaurants,login_page

urlpatterns = [
    path('', home_page ,name='home_page'),
    path('admin/', admin.site.urls,name='admin'),
    path('addrecipies', addrecipies,name='addrecipies'),
    path('addishes', adddishes,name='addishes'),
    path('addrestaurants', addrestaurants,name='addrestaurants'),
    path('login', login_page,name='login'),
    path('register', register_page,name='register'),
    path('details/<int:pk>', detail_view,name='details'),

    path('alldishes', alldishes,name='alldishes'),
    path('allrestaurants', allrestaurants,name='allrestaurants'),
    path('allrecipies', allrecipies, name='allrecipies'),

    path('dish/<int:pk>', dish,name='dish'),
    path('restaurant/<int:pk>', restaurant,name='restaurant'),
    path('recipie/<int:pk>', recipie,name='recipie'),
    path('nnews/<int:pk>', news,name='nnews'),
    path('news', addnews,name='news'),
    path('allnews', allnews,name='allnews'),
    


    path('contact', contact,name='contact'),
    
    
    
]


if settings.DEBUG:
	urlpatterns = urlpatterns +static(settings.STATIC_URL, 
		document_root= settings.STATIC_ROOT)
	urlpatterns = urlpatterns +static(settings.MEDIA_URL, 
		document_root= settings.MEDIA_ROOT)

