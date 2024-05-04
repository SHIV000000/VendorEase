#vendor_management\vendor_management\urls.py


from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render 
from vendors.models import Vendor, PurchaseOrder
from vendors.views import index, vendor_detail, vendor_performance, purchase_order_list, purchase_order_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('vendors.urls')),
    path('', index, name='index'),
]

