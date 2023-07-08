from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.generics import ListCreateAPIView
from rest_framework import status
from .models import Product, Category
from .serializer import CategorySerializer #, ProductSerializer


class CategoryViewSet(ReadOnlyModelViewSet, ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    

