from django.shortcuts import render

from cart.models import Cart
from product.models import *
from user.models import CustomerUser
from cart.models import *
# Create your views here.

# def searchbykey(request,key):

def showproduct(request,userid,productid):
    user = CustomerUser.objects.get(pk = userid)
    variation = Variation.objects.get(pk = productid)
    return callproduct_detail(request,user,variation)
def showproduct_nouser(request,productid):
    variation = Variation.objects.get(pk = productid)
    context = {"item":variation}
    return render(request, 'homepage/product.html', context)
def showall(request,userid,start):
    user = CustomerUser.objects.get(pk = userid)
    return callproduct(request,user,start)
def loadmore(request,userid,start,key):
    start = start +9
    user = user = CustomerUser.objects.get(pk = userid)
    return callproduct(request,user,start)
def loadmore_search(request,userid,start,key):
    start = start +9
    user = CustomerUser.objects.get(pk=userid)
    return callproduct_byname(request, user, start, key)
def loadmore_nouser(request,start):
    start = start+9
    list_var = Variation.objects.all()
    count = 1
    list_resut = []
    for item in list_var:
        if count < start:
            list_resut = []
            count = count + 1
        elif count <= (start + 9):
            list_resut.append(item)
            count = count + 1
    context = {"list_var": list_var, "count": len(list_var), "start": start}
    return render(request, 'homepage/shop.html', context)
def loadmore_nouser_search(request,start,key):
    start = start +9
    list_var = Variation.objects.filter(title__contains=key)
    count = 1
    list_resut = []
    for item in list_var:
        if count < start:
            list_resut = []
            count = count + 1
        elif count <= (start + 9):
            list_resut.append(item)
            count = count + 1
    context = {"list_var": list_resut, "count": len(list_var), "start": start}
    return render(request, 'homepage/shop.html', context)

def showall_nouser(request,start):
    list_var = Variation.objects.filter(pk__gte=start)
    context = {"list_var":list_var,"count":len(list_var),"start":start}
    return render(request,'homepage/shop.html',context)

def addtocart(request,productid,cartid,userid,start):
    variation = Variation.objects.get(pk = productid)
    cart = Cart.objects.get(pk = cartid)
    listproduct  = cart.cartitem_set.all()
    check=True
    for item in listproduct:
        if item.item.id is variation.id :
            CartItem.objects.filter(pk= item.id).update(quantity= item.quantity+1)
            check=False

    if check is True:
        cartitem = CartItem(cart=cart, item=variation, quantity=1)
        cartitem.save()
    user = CustomerUser.objects.get(pk=userid)
    return callproduct(request,user,start)
def removefromcart(request,cartitemid,userid,start):
    item = CartItem.objects.get(pk = cartitemid)
    item.delete()
    user = CustomerUser.objects.get(pk=userid)
    return callproduct(request,user,start)

def searchproduct(request,userid,start):
    key = request.POST.get("key")
    user = CustomerUser.objects.get(pk = userid)
    return callproduct_byname(request,user,start,key)
def searchproductno(request,start):
    key = request.POST.get("key")
    list_var = Variation.objects.filter(title__contains=key)
    count = 1
    list_resut = []
    for item in list_var:
        if count < start:
            list_resut = []
            count = count + 1
        elif count <= (start + 9):
            list_resut.append(item)
            count = count + 1
    context = {"list_var": list_resut, "count": len(list_var), "start": start}
    return render(request, 'homepage/shop.html', context)

def callproduct_detail(request,user,product):
    if Cart.objects.filter(user=user).exists() is False:
        cart = Cart(user=user)
        cart.save()

    else:
        cart = user.cart_set.get(user=user)

    list_cartitem = cart.cartitem_set.all()
    totalmoney = 0
    for itemm in list_cartitem:
        totalmoney = totalmoney + (itemm.quantity * itemm.item.sale_price)
    context = {"item":product,
               "user": user,
               "cart_count": len(list_cartitem),
               "listcart": list_cartitem,
               "total_money": totalmoney,
               "cart": cart}
    return render(request, 'homepage/product.html', context)
def callproduct_byname(request,user,start,key):
    if Cart.objects.filter(user=user).exists() is False:
        cart = Cart(user=user)
        cart.save()

    else:
        cart = user.cart_set.get(user=user)

    list_cartitem = cart.cartitem_set.all()
    totalmoney = 0

    list_var = Variation.objects.filter( title__contains = key)
    count = 1
    list_resut = []
    for item in list_var:
        if count < start:
            list_resut = []
            count = count + 1
        elif count <= (start + 9):
            list_resut.append(item)
            count = count + 1
    for itemm in list_cartitem:
        totalmoney = totalmoney + (itemm.quantity * itemm.item.sale_price)
    context = {"list_var": list_resut,
               "key":key,
               "count": len(list_var),
               "user": user,
               "start": start,
               "cart_count": len(list_cartitem),
               "listcart": list_cartitem,
               "total_money": totalmoney,
               "cart": cart}
    return render(request, 'homepage/shop.html', context)
def callproduct(request,user,start):


    if Cart.objects.filter(user=user).exists() is False:
        cart = Cart(user=user)
        cart.save()

    else:
        cart = user.cart_set.get(user=user)

    list_cartitem = cart.cartitem_set.all()
    totalmoney = 0


    list_var = Variation.objects.all()
    count = 1
    list_resut=[]
    for item in list_var:

        if count < start :
            list_resut =[]
            count = count + 1
        elif count <= (start+9):
            list_resut.append(item)
            count = count+1
    for itemm in list_cartitem:
        totalmoney = totalmoney + (itemm.quantity * itemm.item.sale_price)
    context = {"list_var":list_resut,
               "count":len(list_var),
               "user": user,
               "start":start,
               "cart_count": len(list_cartitem),
               "listcart": list_cartitem,
               "total_money": totalmoney,
               "cart": cart}
    return render(request,'homepage/shop.html',context)