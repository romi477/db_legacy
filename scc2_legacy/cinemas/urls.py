from django.urls import path
from .views import *



urlpatterns = [
    path('', index, name='index'),

    path('allproducts/', ProductsList.as_view(), name='all_products'),

    path('products/', wide_tag_view, name='products_wide'),
    path('products/<w_tag>/', narrow_tag_view, name='products_narrow'),
    path('products/<w_tag>/<n_tag>/', product_list, name='product_list'),

    path('customers/', CustomersList.as_view(), name='all_customers'),

    path('customers/<iso>/<name>/', customer_info, name='customer_info'),
    path('customers/<iso>/<name>/<slug>/', ProductInfo.as_view(), name='product_info'),

]
