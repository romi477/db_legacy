from django.shortcuts import render
from .models import Cinema, Customer
from django.views import generic


def index(request):
    p = Cinema.objects.all()
    lst = []
    for i in p:
        if i.wide_tag not in lst:
            lst.append(i.wide_tag)
    return render(request, 'cinemas/index.html', context={'lst': lst})



class ProductsList(generic.ListView):
    model = Cinema
    context_object_name = 'all_products'
    template_name = 'cinemas/allproducts.html'
    queryset = Cinema.objects.all()
    paginate_by = 35

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
    paginate_by = 35

def customer_info(request, iso, name):
    cus = Customer.objects.get(iso__iexact=iso, name__iexact=name)
    cin = Cinema.objects.filter(owner__name__iexact=name, owner__iso__iexact=iso)
    return render(request, 'cinemas/customer_info.html', context={'customer': cus, 'cinema': cin})




