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

app_name = "product"

urlpatterns = [

    path('showproduct_detail/<int:userid>/<int:productid>', views.showproduct, name="showproduct"),
    path('showproduct_detail_nouser/<int:productid>', views.showproduct_nouser, name="showproductno"),

    path('shop/<int:userid>/<int:start>', views.showall, name="shop"),
    path('loadmore/<int:userid>/<int:start>', views.loadmore, name="loadmore"),
    path('searchproduct/<int:userid>/<int:start>', views.searchproduct, name="searchproduct"),
    path('searchproductno/<int:start>', views.searchproductno, name="searchproductno"),
    path('loadmoreno/<int:start>', views.loadmore_nouser, name="loadmoreno"),
    path('loadmoresearch/<int:userid>/<int:start>/<str:key>', views.loadmore_search, name="loadmoresearch"),
    path('loadmoresearchno/<int:start>/<str:key>', views.loadmore_nouser_search, name="loadmoresearchno"),
    path('shopno/<int:start>', views.showall_nouser, name="shopno"),
    path('addtocart/<int:productid>/<int:cartid>/<int:userid>/<int:start>', views.addtocart, name="addtocart"),
    path('removefromcart/<int:cartitemid>/<int:userid>/<int:start>', views.removefromcart, name="removefromcart"),

]
