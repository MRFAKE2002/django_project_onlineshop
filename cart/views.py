from django.shortcuts import render, get_object_or_404, redirect

from .forms import AddProductToCart
from .cart import Cart
from product.models import Product

def cart_detail_view(request):
    cart = Cart(request)
    
    return render(request, 'cart/cart_detail.html', {'cart': cart})

def add_product_to_cart(request, product_id):
    cart = Cart(request)
    
    product = get_object_or_404(Product, id=product_id)
    
    cart_form = AddProductToCart(request.POST)
    
    if cart_form.is_valid():
        cleaned_data = cart_form.cleaned_data
        
        quantity = cleaned_data['quantity']
        
        cart.add_to_cart(product, quantity)
    
    return redirect('cart:cart_detail')