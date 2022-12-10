from product.models import Product

class Cart:
    def __init__(self, request):
        """
        Initialize a cart if not exist
        """
        self.request = request
        
        self.session = self.request.session
        
        cart = self.session.get('cart')
        
        if not cart:
            cart = self.session['cart'] = {}
        
        self.cart = cart 
        
    def add_to_cart(self, product, quantity=1):
        """
        Add product in cart or change its quantity
        """
        product_id = str(product.id)
        
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity' : quantity}
        else:
            self.cart[product_id]['quantity'] = quantity
        
        self.save()
        
    def remove_from_cart(self, product):
        """
        Remove a product from cart
        """
        product_id = str(product.id)
        
        if product_id in self.cart:
            del self.cart[product_id]
        
        self.save()
    
    def save(self):
        """
        Save things that change in the session 
        """
        self.session.modified = True
    
    def __iter__(self):
        product_id = self.cart.keys()
        
        product_model = Product.objects.filter(id__in=product_id)
        
        cart = self.cart.copy()
        
        for product in product_model:
            cart[str(product.id)]['product_info'] = product_model
        
        for item in self.cart.values():
            yield item        
    
    def __len__(self):
        return len(self.cat.keys())
    
    def clear(self):
        del self.session['cart']
        self.save()
    
    def get_total_price(self):
        product_id = self.cart.keys()
        product_model = Product.objects.filter(id__in=product_id)
        
        return sum(product.price for product in product_model)
     