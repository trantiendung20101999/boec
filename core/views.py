from django.contrib.auth import logout
from django.shortcuts import render
from django.views import View
from user.models import CustomerUser
from product.models import Product,Category,Variation
from cart.views import *
# Create your views here.


class HomeView(View):
    def get(self , request):

        cate_book = Category.objects.filter(title="sach")
        list_book =[];
        for item in cate_book:
            listbook = item.product_set.all()
            for item2 in listbook:
                list_book.append(item2)
        list_var = [];
        for item in list_book:
            variation = Variation.objects.get(pk=item.id)
            list_var.append(variation)

        cate_elec = Category.objects.filter(title="do dien tu")
        list_elec=[];
        for item in cate_elec:
            listelec = item.product_set.all()
            for item2 in listelec:
                list_elec.append(item2)
        list_var2 = [];
        for item in list_elec:
            variation = Variation.objects.get(pk=item.id)
            list_var2.append(variation)

        cate_cloth = Category.objects.filter(title="quanao")
        list_cloth=[];
        for item in cate_cloth:
            listcloth = item.product_set.all()
            for item2 in listcloth:
                list_cloth.append(item2)
        list_var3 = [];
        for item in list_cloth:
            variation = Variation.objects.get(pk=item.id)
            list_var3.append(variation)

        product_sale = Product.objects.get (active=False)

        context = {"list_var":list_var , "list_var2":list_var2 , "list_var3":list_var3,"sale":product_sale}

        return render(request,'homepage/index.html',context)

def showlogin(request):
    return render(request,'homepage/login.html')
def showregis(request):
    return render(request,'homepage/register.html')
def logout_request(request):
    logout(request)
    return render(request,'homepage/login.html')
def showindex2(request,userid):
    user  = CustomerUser.objects.get(pk=userid)
    return call(user,request)

