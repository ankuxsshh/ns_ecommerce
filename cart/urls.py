from django.urls import path
from .views import cart_view, cart_delete, add_to_cart, buy_now, update_cart, checkout

urlpatterns = [
    path('', cart_view, name='cart'),
    path('cart/add_to_cart/<int:id>/', add_to_cart, name='add_to_cart'),
    path('cart_remove/<int:id>', cart_delete, name='cartDelete'),
    path('buy_now/<int:product_id>/', buy_now, name='buy_now'),
    path('cart/update/', update_cart, name='update_cart'),
    path('checkout/', checkout, name='checkout'),
]
