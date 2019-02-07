from .models import Cinema, Customer
from . import forms
from .utils import *
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.views.generic import ListView, DetailView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

def test(request):
    out = f'<div>{request.method}</div>'
    # out = f'<div>{auth.get_user(request)}</div>'
    return HttpResponse(out)


def index(request):
    return render(request, 'cinemas/index.html')

def product_types_view(request):
    queryset = Cinema.objects.values('type')
    product_types_list = sorted(set([i['type'] for i in queryset]))
    return render(request, 'cinemas/product_types.html', context={'product_types_list': product_types_list})

def product_subtypes_view(request, type):
    queryset = Cinema.objects.values('type', 'subtype')
    product_subtypes_list = sorted(set([i['subtype'] for i in queryset if i['type'] == type]))
    return render(request, 'cinemas/product_subtypes.html', context={'product_subtypes_list': product_subtypes_list, 'type': type})

def product_list_view(request, type, subtype):
    product_list = Cinema.objects.filter(type=type, subtype=subtype).order_by('title')
    return render(request, 'cinemas/product_list.html', context={'product_list': product_list, 'type': type, 'subtype': subtype})

def customers_iso_view(request):
    queryset = Customer.objects.values('iso')
    customers_iso_list = sorted(set([i['iso'] for i in queryset]))
    return render(request, 'cinemas/customers_iso.html', context={'customers_iso_list': customers_iso_list})

def customers_name_view(request, iso):
    queryset = Customer.objects.values('iso', 'name')
    customers_name_list = sorted([i['name'] for i in queryset if i['iso'] == iso])
    return render(request, 'cinemas/customers_name.html', context={'customers_name_list': customers_name_list, 'iso': iso})


class ProductsList(ListView):
    model = Cinema
    template_name = 'cinemas/allproducts.html'
    context_object_name = 'all_products'
    paginate_by = 20

    def get_queryset(self):
        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = Cinema.objects.filter(Q(title__icontains=search_query) | Q(owner__name__icontains=search_query))
        else:
            queryset = Cinema.objects.all()
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsList, self).get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search', '')
        context['query_string'] = self.request.META['QUERY_STRING']
        return context


class ProductInfo(DetailView):
    model = Cinema
    template_name = 'cinemas/product_info.html'
    context_object_name = 'product'


class CustomersList(ListView):
    model = Customer
    context_object_name = 'all_customers'
    template_name = 'cinemas/allcustomers.html'
    queryset = Customer.objects.all()
    paginate_by = 20


class CustomerInfo(View):
    def get(self, request, iso, name):
        customer = get_object_or_404(Customer, iso=iso, name=name)
        cinemas = Cinema.objects.filter(owner__name__iexact=name, owner__iso__iexact=iso)
        return render(request, 'cinemas/customer_info.html', context={'customer': customer, 'cinemas': cinemas})


def pick_object(request):
    return render(request, 'cinemas/pick_object.html', {})

class CreateCustomer(LoginRequiredMixin, PermissionRequiredMixin, ObjectCreateMixin, View):
    model_form = forms.CustomerForm
    object_name = 'Customer'
    object_url = 'new_customer'
    permission_required = 'cinemas.create_customer'
    raise_exception = True


class EditCustomer(LoginRequiredMixin, PermissionRequiredMixin, ObjectEditMixin, View):
    model = Customer
    model_form = forms.CustomerForm
    permission_required = 'cinemas.edit_customer'
    raise_exception = True

class DeleteCustomer(LoginRequiredMixin, PermissionRequiredMixin, ObjectDeleteMixin, View):
    model = Customer
    redirect_url = 'customers_iso'
    permission_required = 'cinemas.delete_customer'
    raise_exception = True


class CreateCinema(LoginRequiredMixin, PermissionRequiredMixin, ObjectCreateMixin, View):
    model_form = forms.CinemaForm
    object_name = 'Product'
    object_url = 'new_product'
    permission_required = 'cinemas.create_cinema'
    raise_exception = True


class EditCinema(LoginRequiredMixin, PermissionRequiredMixin, ObjectEditMixin, View):
    model = Cinema
    model_form = forms.CinemaForm
    permission_required = 'cinemas.edit_cinema'
    raise_exception = True


class DeleteCinema(LoginRequiredMixin, PermissionRequiredMixin, ObjectDeleteMixin, View):
    model = Cinema
    redirect_url = 'product_types'
    permission_required = 'cinemas.delete_cinema'
    raise_exception = True


















