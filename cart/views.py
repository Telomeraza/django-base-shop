from django.shortcuts import render, redirect, get_object_or_404    # 31.
from shop.models import Product                                    # 32.
from .cart import Cart                                              # 33.
from .forms import CartAddProductForm                               # 35.
from django.views.decorators.http import require_POST               # 36.

# 37.


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(require_POST)

    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'], override_quantity=cd['override'])
    return redirect('cart:cart_detail')


@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
            initial={'quantity': item['quantity'], 'override': True, })
    return render(request, 'cart/detail.html', {'cart': cart})
