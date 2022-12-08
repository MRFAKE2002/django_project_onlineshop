from django.shortcuts import render

from django.views import generic

from product.models import Product

class HomePageView(generic.ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'


class ContactUsPageView(generic.TemplateView):
    template_name = 'contact_us.html'

