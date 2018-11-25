from django.urls import path
from django.conf.urls import url
from .views import *



urlpatterns = [
    path('', index, name='index'),
    path('products/', ProductsList.as_view(), name='products'),
    # path('products/<narrow_tag>', narrow_tag_list, name='narrow_tag_list'),
    path('customers/', CustomersList.as_view(), name='customers'),
    path('customers/<iso>/<name>', customer_info, name='customer_info'),
    path('products/<iso>/<name>/<uniqueid>', ProductInfo.as_view(), name='product_info'),
    # path('products/<pk>/<slug>', ProductInfo.as_view(), name='product_info'),
]
