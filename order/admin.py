from django.contrib import admin
from order.models import Order,Orderlist,Orderitem
# Register your models here

admin.site.register(Order)
admin.site.register(Orderlist)
admin.site.register(Orderitem)

