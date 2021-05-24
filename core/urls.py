"""shopp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from . import views
from .views import HomeView

app_name = "core"

urlpatterns = [

    path('', HomeView.as_view() , name="index"),
    path('login/', views.showlogin , name="login"),
    path('order/', views.showlogin, name="login"),
    path('register/', views.showregis, name="register"),
    path('logout/',views.logout_request,name="logout"),
    path('/<int:userid>', views.showindex2, name="index2"),

]
