from django.shortcuts import render, get_object_or_404, redirect

from .forms import AddProductToCart
from .cart import Cart
from product.models import Product

def cart_detail_view(request):
    cart = Cart(request)
    
    for item in cart:
        item['inplace_product_quantity'] = AddProductToCart(initial={
            'quantity': item['quantity'],
            'inplace': True,
        })
    
    return render(request, 'cart/cart_detail.html', {'cart': cart})

def add_product_to_cart(request, product_id):
    cart = Cart(request)
    
    product = get_object_or_404(Product, id=product_id)
    
    cart_form = AddProductToCart(request.POST)
    
    if cart_form.is_valid():
        cleaned_data = cart_form.cleaned_data
        
        quantity = cleaned_data['quantity']
        
        replace_current_quantity = cleaned_data['inplace']
        
        cart.add_to_cart(product, quantity, replace_current_quantity)
    
    return redirect('cart:cart_detail')

def remove_from_cart(request, product_id):
    cart = Cart(request)
    
    product = get_object_or_404(Product, id=product_id)

    cart.remove_from_cart(product)
        
    return redirect('cart:cart_detail')
