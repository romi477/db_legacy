from django.shortcuts import render
from .models import Cinema, Customer
from django.views import generic


def index(request):

    return render(request, 'cinemas/index.html')

def wide_tag_view(request):
    queryset = Cinema.objects.values('wide_tag')
    wide_tag_list = [i['wide_tag'] for i in queryset]
    return render(request, 'cinemas/products_wide_tag.html', context={'wide_product_list': set(wide_tag_list)})


def narrow_tag_view(request, w_tag):
    queryset = Cinema.objects.values('wide_tag', 'narrow_tag')
    narrow_tag_list = [i['narrow_tag'] for i in queryset if i['wide_tag'] == w_tag]
    return render(request, 'cinemas/products_narrow_tag.html', context={'narrow_product_list': set(narrow_tag_list), 'wtag': w_tag})

def product_list(request, w_tag, n_tag):
    queryset = Cinema.objects.values('title', 'narrow_tag')
    prod_list = [i['title'] for i in queryset if i['narrow_tag'] == n_tag]
    return render(request, 'cinemas/product_list.html', context={'product_list': prod_list})



class ProductsList(generic.ListView):
    model = Cinema
    context_object_name = 'all_products'
    template_name = 'cinemas/allproducts.html'
    queryset = Cinema.objects.all()
    paginate_by = 20


class ProductInfo(generic.DetailView):
    model = Cinema
    template_name = 'cinemas/product_info.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super(ProductInfo, self).get_context_data(**kwargs)
        context['custom_list'] = Customer.objects.all()
        return context


class CustomersList(generic.ListView):
    model = Customer
    context_object_name = 'all_customers'
    template_name = 'cinemas/allcustomers.html'
    queryset = Customer.objects.all()
    paginate_by = 20

def customer_info(request, iso, name):
    cus = Customer.objects.get(iso__iexact=iso, name__iexact=name)
    cin = Cinema.objects.filter(owner__name__iexact=name, owner__iso__iexact=iso)
    return render(request, 'cinemas/customer_info.html', context={'customer': cus, 'cinema': cin})




