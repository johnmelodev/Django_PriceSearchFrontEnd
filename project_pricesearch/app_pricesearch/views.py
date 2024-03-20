from django.shortcuts import render
from .models import Product


def search(request):
    return render(request, 'products/search.html')


def show_results(request):
    product_name = request.POST.get('product')
    print(product_name)
    datas = {
        'datas': Product.objects.filter(name__icontains=product_name).order_by('price')
    }

    return render(request, 'products/search_results.html', datas)
