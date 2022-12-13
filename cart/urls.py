from django.urls import path 

from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail_view, name='cart_detail'),
    path('add_cart/<int:product_id>', views.add_product_to_cart, name='add_to_cart'),
    path('remove_cart/<int:product_id>', views.remove_from_cart, name='remove_from_cart'),
]