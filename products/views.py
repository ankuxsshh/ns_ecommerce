from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from .models import Products
from cart.models import Cart

# Create your views here.

def shop_view(request,cat):
    if cat == 'All':
        products = Products.objects.all()
        context = {
            'products': products,
            'cat': "All Products"
        }
        
        return render(request, 'shop.html', context=context)
    else:
        products = Products.objects.filter(type=cat)
        context = {
            'products': products,
            'cat': cat.upper()
        }
                
        return render(request, 'shop.html', context=context)
    
    # products = Products.objects.all()
    
    # context = {
    #     'products': products
    # }

    # return render(request, 'shop.html', context=context)

def detail_view(request,id):
    product = Products.objects.get(id=id)
    # print(product.id)
    cat = product.type
    related = Products.objects.filter(type=cat)[:4]
    if request.method == 'POST':
        # pid = request.POST['product']
        if request.POST['addCart'] == 'addtocart':
            qty = request.POST['qty'] 
            
            addProduct = Cart(add_user=request.user,pid=id,item_title=product.title,qty=qty,rate=product.price,sub_total=(int(qty)*int(product.price)))
            if request.user.is_authenticated:
                addProduct.save()
                arg_list = [id]
                messages.success(request,"Item added to cart.")
                return redirect(reverse('single_product',args=arg_list))
                # return render(request, 'single-product.html', {'product':product,'related':related,'itemadded':True})
        elif request.POST['buy'] == 'buynow':
            pass
    return render(request, 'single-product.html', {'product':product,'related':related})