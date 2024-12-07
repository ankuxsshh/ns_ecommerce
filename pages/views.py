from django.shortcuts import render, redirect
from products.models import Products

# Create your views here.

def home_view(request):

    products = Products.objects.all()[:8]
    new_products = Products.objects.all()[:4]

    context = {
        'products': products,
        'new_products': new_products
    }
    return render(request, 'index.html', context=context)

def about_view(request):


    context = {

    }
    return render(request, 'about.html', context=context)