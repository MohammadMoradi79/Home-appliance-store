from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from .models import Product, Category, Customer
from .serializer import CategorySerializer, ProductSerializer, CustomerSerializer


class CategoryViewSet(ModelViewSet):
    def get_queryset(self, parent=False):
        queryset = Category.objects.all()
        if parent:
            queryset = Category.objects.filter(parent__isnull=parent)
        return queryset

    serializer_class = CategorySerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset(parent=True)
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
