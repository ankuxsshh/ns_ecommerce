from django.shortcuts import render, get_object_or_404, redirect
from cart.models import Cart
from products.models import Product, ProductQuantity
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url="user_login/")
def cart_view(request):
    items = Cart.objects.filter(add_user=request.user.username).order_by('-id')
    total = sum(item.sub_total for item in items)
    view_cart_button = False  # Flag to track if 'Buy Now' was clicked
    
    # Check if the user has recently added something via 'Buy Now'
    if 'view_cart_button' in request.session and request.session['view_cart_button']:
        view_cart_button = True
        del request.session['view_cart_button']  # Clear the flag after use

    context = {
        'items': items,
        'cart_total': total,
        'view_cart_button': view_cart_button,
    }
    return render(request, 'cart.html', context)


@login_required(login_url="user_login/")
def add_to_cart(request, id):
    # Fetch the product
    product = get_object_or_404(Product, id=id)

    # Retrieve the default quantity for the product (e.g., first available option)
    product_quantity = product.quantities.first()

    if not product_quantity:
        messages.error(request, "The selected product is currently unavailable.")
        return redirect('cart')

    if request.method == 'POST':
        # Create or update the cart item
        cart_item, created = Cart.objects.get_or_create(
            pid=product_quantity.id,
            add_user=request.user.username,
            defaults={
                'item_title': f"{product.title} - {product_quantity.quantity}",
                'qty': 1,
                'rate': product_quantity.price,
                'sub_total': product_quantity.price,
            }
        )
        if not created:
            cart_item.qty += 1
            cart_item.sub_total = cart_item.qty * cart_item.rate
            cart_item.save()

        messages.success(request, f"{product.title} ({product_quantity.quantity}) successfully added to the cart.")
        return redirect('cart')

@login_required(login_url="user_login/")
def cart_delete(request, id):
    item = get_object_or_404(Cart, id=id, add_user=request.user.username)
    item.delete()
    return redirect('cart')

@login_required(login_url="user_login/")
def buy_now(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product_quantity = product.quantities.first()

    # Check if product quantity is available
    if not product_quantity:
        messages.error(request, "The selected product is currently unavailable.")
        return redirect('cart')

    # Add the product to the cart
    cart_item, created = Cart.objects.get_or_create(
        pid=product_quantity.id,
        add_user=request.user.username,
        defaults={
            'item_title': f"{product.title} - {product_quantity.quantity}",
            'qty': 1,
            'rate': product_quantity.price,
            'sub_total': product_quantity.price,
        }
    )

    # If the product is already in the cart, just increase the quantity
    if not created:
        cart_item.qty += 1
        cart_item.sub_total = cart_item.qty * cart_item.rate
        cart_item.save()

    # Notify the user and redirect to the cart page
    messages.success(request, f"{product.title} ({product_quantity.quantity}) successfully added to the cart.")
    return redirect('cart')  # Redirect to the cart page after adding the product


