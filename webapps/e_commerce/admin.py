from django.contrib import admin
from webapps.e_commerce.models import *

# Register your models here.


admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(UserProfile)
