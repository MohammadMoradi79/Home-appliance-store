from rest_framework import serializers
from .models import Category, Product, Customer, Comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', 'children']

    def to_representation(self, category):
        self.fields['children'] = CategorySerializer(many=True, read_only=True)
        return super(CategorySerializer, self).to_representation(category)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['category', 'title', 'price', 'pk']

    price = serializers.DecimalField(max_digits=6, decimal_places=2, source='unit_price')


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'pk']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['product', 'customer', 'content', 'placed_at']
