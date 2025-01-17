from django.shortcuts import render, redirect, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse
from products.models import Product  # Corrected import
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

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from products.models import Product
from cart.models import Cart

# Create your views here.

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

    # Fetch related products by category
    related = Product.objects.filter(type=product.type)[:4]

    # Handling cart addition
    if request.method == 'POST':
        if request.POST.get('addCart') == 'addtocart':
            qty = request.POST['qty']
            addProduct = Cart(
                add_user=request.user,
                pid=id,
                item_title=product.title,
                qty=qty,
                rate=product.price,
                sub_total=(int(qty) * int(product.price))
            )
            if request.user.is_authenticated:
                addProduct.save()
                messages.success(request, f"{product.title} added to cart with quantity {qty}.")
                return redirect('cart')  # Redirect to cart page after adding to the cart
        elif request.POST.get('buy') == 'buynow':
            pass

    return render(request, 'single-product.html', {
        'product': product,
        'related': related,
        'product_250': product_250,
        'product_500': product_500,
        'images_250': images_250,
        'images_500': images_500,
        'in_stock': in_stock,  # Passing in_stock to the template
    })
