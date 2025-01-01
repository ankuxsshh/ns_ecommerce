from django.shortcuts import render
from products.models import Product, ProductQuantity
# Create your views here.

def home_view(request):
    # Fetching bestseller products (example: products with highest price as bestsellers)
    bestsellers = ProductQuantity.objects.all().order_by('-price')[:8]

    # Fetching new products (example: products added recently)
    new_products = ProductQuantity.objects.all().order_by('-id')[:4]

    context = {
        'bestsellers': bestsellers,
        'new_products': new_products,
    }
    return render(request, 'index.html', context=context)

def about_view(request):
    context = {}
    return render(request, 'about.html', context=context)
