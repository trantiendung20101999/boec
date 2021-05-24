from django.db import models
from user.models import CustomerUser
from cart.models import Cart
from product.models import *
# Create your models here.
class Orderlist(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
class Order(models.Model):
    user = models.ForeignKey(CustomerUser,on_delete=models.CASCADE)
    orderlist = models.ForeignKey(Orderlist,on_delete=models.CASCADE,default='')
    shipping_address = models.CharField(max_length=255,default='')
    order_description = models.TextField(default='')
    is_completed = models.BooleanField(default=False)
class Orderitem(models.Model):
    orderlist = models.ForeignKey(Orderlist, on_delete=models.CASCADE)
    item = models.ForeignKey(Variation, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)