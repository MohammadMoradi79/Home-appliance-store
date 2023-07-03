from rest_framework import serializers
from .models import Category

class ProductSerializer(serializers.Serializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all()
    )
    category_title = serializers.StringRelatedField(source='category')
    title = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=6, decimal_places=2, source='unit_price')



