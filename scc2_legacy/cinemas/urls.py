from django.urls import path
from .views import *



urlpatterns = [
    path('test/  ', test, name='test'),
    path('', index, name='index'),

    path('allproducts/', ProductsList.as_view(), name='all_products'),

    path('products/', product_types_view, name='product_types'),
    path('products/<type>/', product_subtypes_view, name='product_subtypes'),
    path('products/<type>/<subtype>/', product_list_view, name='product_list'),
    path('products/<type>/<subtype>/<slug>/', ProductInfo.as_view(), name='product_info'),
    path('products/<type>/<subtype>/<slug>/edit/', EditCinema.as_view(), name='product_edit'),
    path('products/<type>/<subtype>/<slug>/delete/', DeleteCinema.as_view(), name='product_delete'),

    path('allcustomers/', CustomersList.as_view(), name='all_customers'),

    path('customers/', customers_iso_view, name='customers_iso'),

    path('customers/<iso>/', customers_name_view, name='customers_name'),
    path('customers/<iso>/<name>/', CustomerInfo.as_view(), name='customer_info'),
    path('customers/<iso>/<name>/edit/', EditCustomer.as_view(), name='customer_edit'),
    path('customers/<iso>/<name>/delete/', DeleteCustomer.as_view(), name='customer_delete'),

    path('forms/', pick_object, name='pick_new_object'),

    path('forms/add-customer/', CreateCustomer.as_view(), name='new_customer'),
    path('forms/add-cinema/', CreateCinema.as_view(), name='new_cinema'),
]
