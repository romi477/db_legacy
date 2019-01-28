from .models import Cinema, Customer
from . import forms
from django.shortcuts import redirect, reverse
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.views.generic import ListView, DetailView
from django.views import View

def test(request):
    out = f'<div>{request.META["QUERY_STRING"]}</div>'
    return HttpResponse(out)
    # d = request.META.items()
    # return render(request, 'cinemas/test.html', context={'d': d})


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
    paginate_by = 9

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
        # context['query_string'] = self.request.META['QUERY_STRING']
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
    paginate_by = 9


class CustomerInfo(View):
    def get(self, request, iso, name):
        customer = get_object_or_404(Customer, iso=iso, name=name)
        cinemas = Cinema.objects.filter(owner__name__iexact=name, owner__iso__iexact=iso)
        return render(request, 'cinemas/customer_info.html', context={'customer': customer, 'cinemas': cinemas})


def pick_object(request):
    return render(request, 'cinemas/pick_object.html', {})


class CreateCustomer(View):
    def get(self, request):
        model_form = forms.CustomerForm()
        return render(request, 'cinemas/add_object.html', {'model_form': model_form, 'object_url': 'new_customer'})

    def post(self, request):
        bound_form = forms.CustomerForm(request.POST)

        if bound_form.is_valid():
            customer = bound_form.save()
            return redirect(customer)
        return render(request, 'cinemas/add_object.html', {'model_form': bound_form, 'object_url': 'new_customer'})


class EditCustomer(View):
    def get(self, request, iso, name):
        customer = Customer.objects.get(iso=iso, name=name)
        bound_form = forms.CustomerForm(instance=customer)
        return render(request, 'cinemas/edit_object.html', {'model_form': bound_form, 'model': customer})

    def post(self, request, iso, name):
        customer = Customer.objects.get(iso=iso, name=name)
        bound_form = forms.CustomerForm(request.POST, instance=customer)

        if bound_form.is_valid():
            edit_customer = bound_form.save()
            return redirect(edit_customer)
        else:
            return render(request, 'cinemas/add_object.html', {'model_form': bound_form, 'model': customer})


class DeleteCustomer(View):
    def get(self, request, iso, name):
        customer = Customer.objects.get(iso=iso, name=name)
        return render(request, 'cinemas/delete_object.html', {'model': customer})

    def post(self, request, iso, name):
        customer = Customer.objects.get(iso=iso, name=name)
        customer.delete()
        return redirect('customers_name', iso=iso)



class CreateCinema(View):
    def get(self, request):
        model_form = forms.CinemaForm()
        return render(request, 'cinemas/add_object.html', {'model_form': model_form, 'object_url': 'new_cinema'})

    def post(self, request):
        bound_form = forms.CinemaForm(request.POST)

        if bound_form.is_valid():
            cinema = bound_form.save()
            return redirect(cinema)
        return render(request, 'cinemas/add_object.html', {'model_form': bound_form, 'object_url': 'new_cinema'})


class EditCinema(View):
    def get(self, request, type, subtype, slug):
        cinema = Cinema.objects.get(type=type, subtype=subtype, slug=slug)
        bound_form = forms.CinemaForm(instance=cinema)
        return render(request, 'cinemas/edit_object.html', {'model_form': bound_form, 'model': cinema})

    def post(self, request, type, subtype, slug):
        cinema = Cinema.objects.get(type=type, subtype=subtype, slug=slug)
        bound_form = forms.CinemaForm(request.POST, instance=cinema)

        if bound_form.is_valid():
            edit_cinema = bound_form.save()
            return redirect(edit_cinema)
        else:
            return render(request, 'cinemas/add_object.html', {'model_form': bound_form, 'model': cinema})


class DeleteCinema(View):
    def get(self, request, type, subtype, slug):
        cinema = Cinema.objects.get(type=type, subtype=subtype, slug=slug)
        return render(request, 'cinemas/delete_object.html', {'model': cinema})

    def post(self, request, type, subtype, slug):
        cinema = Cinema.objects.get(type=type, subtype=subtype, slug=slug)
        cinema.delete()
        return redirect('customer_info', iso=cinema.owner.iso, name=cinema.owner.name)



















