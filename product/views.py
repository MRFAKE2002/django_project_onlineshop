from django.shortcuts import render
from django.views import generic


from .models import Product

class ProductListView(generic.ListView):
    # We use queryset for add or change something that are in our databases in our code
    queryset = Product.objects.filter(active=True)
    paginate_by = 4
    template_name = 'products/product_list.html'
    context_object_name = 'products'


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'products/product_details.html'

