from django.shortcuts import render
from django.db.models import Max, F, Func
from warehouse.models import Product, Category


def hello_world(request):
    # product = Product()
    # product.category = Category(pk=2)
    # product.title = 'Washing Machin'
    # product.unit_price = 10
    # product.save()

    query_set = Product.objects.filter(id__range=(90, 102))

    return render(request, 'hello.html', {'name': 'Mohammad', 'result': list(query_set)})