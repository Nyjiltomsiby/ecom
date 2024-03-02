from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse
from .models import Product, Category  # Import both models

# Create your views here.
def allproducts(request, slug_c=None):
    page_c = None
    products = None
    if slug_c:
        page_c = get_object_or_404(Category, slug=slug_c)
        products = Product.objects.filter(category=page_c, available=True)
    else:
        products = Product.objects.filter(available=True)

    return render(request, 'home.html', {'category': page_c, 'products': products})


def prod_det(request, slug_c, slug_p):
    try:
        product = Product.objects.get(category__slug=slug_c, slug=slug_p)
    except Product.DoesNotExist:
        raise Http404("Product does not exist")
    return render(request, 'product.html', {'product': product})  


def navbar(request):
    return render(request, 'navbar.html')
