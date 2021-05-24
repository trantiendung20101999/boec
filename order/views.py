from django.shortcuts import render
from cart.models import *
from user.models import *
from product.models import *
from order.models import *
from cart.views import *
# Create your views here.

def showcheckout(request,userid):
    myuser = CustomerUser.objects.get(pk=userid)
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
    return render(request, 'homepage/check-out.html', context)
def createorder(request,userid):
    myuser = CustomerUser.objects.get(pk=userid)
    if Cart.objects.filter(user=myuser).exists() is False:
        cart = Cart(user=myuser)
        cart.save()

    else:
        cart = myuser.cart_set.get(user=myuser)
    firstname = request.POST.get("first_name")
    lastname = request.POST.get("last_name")
    address = request.POST.get("address")
    email = request.POST.get("email")
    phone = request.POST.get("phone")
    des = "Họ : "+firstname+"\n"+"Tên: "+lastname+"\n"+"Email: "+email+"\n"+"Phone: "+phone+"\n"
    orderlist = Orderlist()
    orderlist.save()
    list_cartitem = cart.cartitem_set.all()
    for item in list_cartitem:
        orderItem = Orderitem(orderlist=orderlist,item=item.item,quantity=item.quantity)
        orderItem.save()
    order = Order(user = myuser,orderlist=orderlist, shipping_address=address,order_description=des, is_completed=False)
    order.save()
    cart.delete()
    return call(myuser, request)
