from django.core.paginator import Paginator
from django.http import HttpRequest
from django.shortcuts import render
from catalog.models import Product


def product_list(request):
    product_list = Product.objects.all().order_by('id')
    paginator = Paginator(product_list, 6)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    custom_page_range = paginator.get_elided_page_range(page_obj.number, on_each_side=1, on_ends=1)

    return render(request, 'catalog/home.html', {
        'page_obj': page_obj,
        'page_range': custom_page_range
    })


def contacts(request):
    if request.method == 'GET':
        return render(request, 'catalog/contacts.html')
    return None


def get_product(request: HttpRequest, product_id: int):
    product = Product.objects.get(id=product_id)
    context = {'product': product}
    return render(request, 'catalog/product.show.html', context)
