from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Category
from .serializer import ProductSerializer


@api_view()
def product_list(request):
    product = Product.objects.select_related('category').all()
    serializer = ProductSerializer(product, many=True)
    return Response(serializer.data)

