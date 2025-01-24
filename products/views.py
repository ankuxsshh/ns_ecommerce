from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from products.models import Product
from cart.models import Cart

# Create your views here.

def shop_view(request, cat):
    if cat == 'All':
        products = Product.objects.all()
        context = {
            'bestsellers': products,  # Pass all products as bestsellers
            'cat': "ALL PRODUCTS"
        }
    else:
        products = Product.objects.filter(type=cat)
        context = {
            'bestsellers': products,  # Pass filtered products based on category
            'cat': cat.upper()  # Display category name (e.g., "CASHEW")
        }
    
    return render(request, 'shop.html', context=context)

def detail_view(request, id):
    product = Product.objects.get(id=id)
    
    # Fetching quantity and images using the correct related_name
    product_250 = product.quantities.filter(quantity='250g').first()
    product_500 = product.quantities.filter(quantity='500g').first()

    # Get the images for each quantity type (if available)
    images_250 = product_250.images.all() if product_250 else []
    images_500 = product_500.images.all() if product_500 else []

    # Check availability of any quantity (either 250g or 500g)
    in_stock = False
    if product_250 and product_250.availability == 'In Stock':
        in_stock = True
    if product_500 and product_500.availability == 'In Stock':
        in_stock = True

    # Handling cart addition
    if request.method == 'POST':
        qty = request.POST.get('qty', 1)  # Get quantity from form (default to 1)
        qty = int(qty)  # Convert to integer

        if request.POST.get('add_to_cart'):  # Check if the form is for "Add to Cart"
            product_quantity = product_500 if product_500 else product_250
            if not product_quantity or product_quantity.availability != 'In Stock':
                messages.error(request, "The selected product is out of stock.")
                return redirect('product_detail', id=id)

            # Create or update the cart item
            cart_item, created = Cart.objects.get_or_create(
                pid=product.id,
                add_user=request.user,
                defaults={'item_title': product.title, 'qty': qty, 'rate': product_quantity.price}
            )
            if not created:
                cart_item.qty += qty  # Update quantity if already in cart
                cart_item.save()

            cart_item.sub_total = cart_item.qty * cart_item.rate
            cart_item.save()
            messages.success(request, f"{product.title} added to cart.")
            return redirect('cart')

    return render(request, 'single-product.html', {
        'product': product,
        'product_250': product_250,
        'product_500': product_500,
        'images_250': images_250,
        'images_500': images_500,
        'in_stock': in_stock,
    })