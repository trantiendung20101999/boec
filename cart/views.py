from django.shortcuts import render, redirect
from cart.models import *
from product.models import *
from user.models import *
# Create your views here.


def showcart(request,userid):

    myuser = CustomerUser.objects.get(pk = userid)
    if Cart.objects.filter(user=myuser).exists() is False:
        cart = Cart(user=myuser)
        cart.save()

    else:
        cart = myuser.cart_set.get(user=myuser)

    list_cartitem = cart.cartitem_set.all()
    totalmoney = 0
    for itemm in list_cartitem:
        totalmoney = totalmoney + (itemm.quantity * itemm.item.sale_price)
    context = {
               "user": myuser, "cart_count": len(list_cartitem),
               "listcart": list_cartitem, "total_money": totalmoney, "cart": cart}
    return render(request, 'homepage/shopping-cart.html', context)
def addtocart(request,productid,cartid,userid):
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
    return call(user,request)
def removefromcart(request,cartitemid,userid):
    item = CartItem.objects.get(pk = cartitemid)
    item.delete()
    user = CustomerUser.objects.get(pk=userid)
    return call(user,request)
def call(myuser,request):
    cate_book = Category.objects.filter(title="sach")
    list_book = [];

    for item in cate_book:
        listbook = item.product_set.all()
        for item2 in listbook:
            list_book.append(item2)
    list_var = [];
    for item in list_book:
        variation = Variation.objects.get(pk=item.id)
        list_var.append(variation)

    cate_elec = Category.objects.filter(title="do dien tu")
    list_elec = [];
    for item in cate_elec:
        listelec = item.product_set.all()
        for item2 in listelec:
            list_elec.append(item2)
    list_var2 = [];
    for item in list_elec:
        variation = Variation.objects.get(pk=item.id)
        list_var2.append(variation)

    cate_cloth = Category.objects.filter(title="quanao")
    list_cloth = [];
    for item in cate_cloth:
        listcloth = item.product_set.all()
        for item2 in listcloth:
            list_cloth.append(item2)
    list_var3 = [];
    for item in list_cloth:
        variation = Variation.objects.get(pk=item.id)
        list_var3.append(variation)

    product_sale = Product.objects.get(active=False)

    if Cart.objects.filter(user = myuser).exists() is False:
        cart = Cart(user = myuser)
        cart.save()

    else:
        cart = myuser.cart_set.get(user=myuser)

    list_cartitem = cart.cartitem_set.all()
    totalmoney = 0
    for itemm in list_cartitem:
        totalmoney = totalmoney + (itemm.quantity * itemm.item.sale_price)
    context = {"list_var": list_var, "list_var2": list_var2, "list_var3": list_var3, "sale": product_sale,
               "user": myuser, "cart_count": len(list_cartitem),
               "listcart": list_cartitem, "total_money": totalmoney, "cart": cart}
    return render(request, 'homepage/index.html',context)
