from rest_framework import serializers
from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', 'children']

    def to_representation(self, category):
        self.fields['children'] = CategorySerializer(many=True, read_only=True)
        return super(CategorySerializer, self).to_representation(category)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model : Product
        fields = ['category', 'title', 'price']

    price = serializers.DecimalField(max_digits=6, decimal_places=2, source='unit_price')
