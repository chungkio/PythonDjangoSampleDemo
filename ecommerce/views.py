from django.shortcuts import render
from django.db.models import Q
from django.http import Http404
from .models import Product

# Create your views here.
def list(request):
    # if 's' in request.GET and request.GET['product-name']:
    #     text = request.GET.get('product-name')
    #     if text != '':
    #         Data = {'Productss': Products.objects.filter(Q(title__icontains = text)) }
    # else:
    #     Data = {'Productss': Products.objects.all().order_by('-date')}
    return render(request, 'ecommerce/list-product.html')


def Products(request, slug):
    Products = Product.objects.get(slug=slug)
    try:
        Products = Product.objects.get(slug=slug)
    except Products.DoesNotExist:
        raise Http404("Product not found")
    
    return render(request, 'ecommerce/product.html', {'Products': Products})


def categories(request):
    pass


def checkout(request):
    return render(request, 'ecommerce/checkout.html')


def cart(request):
    return render(request, 'ecommerce/cart.html')

def order(request):
    return render(request, 'ecommerce/order.html')