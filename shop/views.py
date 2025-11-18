from django.shortcuts import render, get_object_or_404   # 12.
from .models import Category, Product                    # 13.

# Create your views here.


def product_list(request, category_slug=None):          # 14.
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    category = None
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        # Фильтр категорий от пользователя
        products = products.filter(category=category)

    return render(request, 'product/list.html', {'category': category, 'categories': categories, 'products': products})

# 15. Создать папку templates - shop - product - list.html и заполнить его
# 16. Создать в папке shop файл base.html и заполнить его
# 17. перейти в файл urls в папке base


def product_detail(request, id, slug):              # 20.
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    related_products = Product.objects.filter(
        category=product.category, available=True).exclude(id=product.id)[:4]
    return render(request, 'product/detail.html', {'product': product, 'related_products': related_products})
