from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages

from .forms import CommentForm
from .models import Product, Comment
from cart.forms import AddProductToCart

class ProductListView(generic.ListView):
    # We use queryset for add or change something that are in our databases in our code
    queryset = Product.objects.filter(active=True)
    paginate_by = 4
    template_name = 'products/product_list.html'
    context_object_name = 'products'


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'products/product_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['comment_form'] = CommentForm()
        
        context['add_to_cart'] = AddProductToCart()

        return context


class CommentCreateView(generic.CreateView):
    model = Comment
    form_class = CommentForm
    
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        
        product_id = self.kwargs['product_id']
        obj.product = get_object_or_404(Product, id=product_id)
                
        messages.success(self.request, _('comment created successfully.' ))         

        return super().form_valid(form)
        