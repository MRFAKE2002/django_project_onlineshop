from django.shortcuts import render
from django.views import generic


from .models import Product

class ProductListView(generic.ListView):
    pass
    # queryset =
    