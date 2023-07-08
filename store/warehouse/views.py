from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from .models import Product, Category
from .serializer import CategorySerializer, ProductSerializer


class CategoryViewSet(ModelViewSet):
    def get_queryset(self):
        queryset = Category.objects.filter(parent__isnull=True)
        return queryset
    serializer_class = CategorySerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    