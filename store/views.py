from django.shortcuts import render
from products.models import Product

def home(request):

    products = Product.objects.all().filter( is_featured=True).order_by('-created_date')[:8]
    context= {
        'products': products
    }
    return render(request,'home.html',context)