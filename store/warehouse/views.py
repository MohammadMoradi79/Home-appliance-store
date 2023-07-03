from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Category
from .serializer import CategorySerializer #, ProductSerializer


@api_view()
def category_list(request):
    category = Category.objects.filter(parent__isnull=True)
    serializer = CategorySerializer(category, many=True)
    return Response(serializer.data)

