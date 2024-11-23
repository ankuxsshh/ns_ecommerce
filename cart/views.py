from django.shortcuts import render, get_object_or_404, redirect
from .models import Cart
from products.models import Products
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="user_login/")

def cart_view(request):
    items = Cart.objects.filter(add_user=request.user).order_by('-id')
    total = 0
    for sum in items:
        total += int(sum.sub_total)
    # print(total)
    if request.method == 'POST':
        if request.POST['btn'] == 'update':
            # new_qty = {}
            for item in items:
                new_qty = int(request.POST.get(str(item.id)) )
                if item.qty != new_qty:
                    item.qty = new_qty 
                    item.sub_total = new_qty*item.rate
                    item.save()
            return redirect('cart')
    context = {
        'items': items,
        'cart_total': total
    }
    return render(request, 'cart.html',context)

def cart_delete(request,id):
    item = Cart.objects.get(id=id)
    if request.user.is_authenticated:
        item.delete()
        return redirect('cart')

    return render(request, 'cart.html')
