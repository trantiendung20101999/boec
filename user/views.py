import sys
import traceback

from django.shortcuts import render
from user.models import CustomerUser
from cart.models import Cart,CartItem
from product.models import *
from cart.views import call
# Create your views here.

from django.contrib.auth import authenticate,login


def register(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    repassword = request.POST.get("repassword")

    if CustomerUser.objects.filter(username = username).exists() is False:
        user = CustomerUser.objects.create_user(username=username, password=password)
        user.save()
        context = {"warning": "Đăng ký thành công"}
        return render(request,'homepage/login.html',context)
    elif(password != repassword):
        context = {"warning": "Nhập lại mật khẩu không chính xác"}
    else:
        context = {"warning": "Tài khoản đã tồn tại "}

    return render(request, 'homepage/register.html', context)

def checklogin(request):
    username=request.POST.get("username")
    password = request.POST.get("password")
    myuser = authenticate(username=username, password = password)
    context = {"warning":"Tài khoản hoặc mật khẩu không chính xác"}
    if myuser is None:
        return render(request,'homepage/login.html',context)
    login(request,myuser)
    return call(myuser,request)

    # cate_book = Category.objects.filter(title="sach")
    # list_book = [];
    #
    # for item in cate_book:
    #     listbook = item.product_set.all()
    #     for item2 in listbook:
    #         list_book.append(item2)
    # list_var = [];
    # for item in list_book:
    #     variation = Variation.objects.get(pk=item.id)
    #     list_var.append(variation)
    #
    # cate_elec = Category.objects.filter(title="do dien tu")
    # list_elec = [];
    # for item in cate_elec:
    #     listelec = item.product_set.all()
    #     for item2 in listelec:
    #         list_elec.append(item2)
    # list_var2 = [];
    # for item in list_elec:
    #     variation = Variation.objects.get(pk=item.id)
    #     list_var2.append(variation)
    #
    # cate_cloth = Category.objects.filter(title="quanao")
    # list_cloth = [];
    # for item in cate_cloth:
    #     listcloth = item.product_set.all()
    #     for item2 in listcloth:
    #         list_cloth.append(item2)
    # list_var3 = [];
    # for item in list_cloth:
    #     variation = Variation.objects.get(pk=item.id)
    #     list_var3.append(variation)
    #
    # product_sale = Product.objects.get(active=False)
    #
    # cart =  myuser.cart_set.get(user=myuser)
    # list_cartitem = cart.cartitem_set.all()
    # totalmoney=0
    # for itemm in list_cartitem:
    #     totalmoney = totalmoney + (itemm.quantity * itemm.item.sale_price)
    # context = {"list_var": list_var, "list_var2": list_var2, "list_var3": list_var3, "sale": product_sale, "user":myuser,"cart_count":len(list_cartitem),
    #            "listcart" : list_cartitem,"total_money":totalmoney , "cart":cart}
    # return render(request, 'homepage/index.html',context)

