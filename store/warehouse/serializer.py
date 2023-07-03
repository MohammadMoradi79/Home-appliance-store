from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', 'children']

    def to_representation(self, category):
        self.fields['children'] = CategorySerializer(many=True, read_only=True)
        return super(CategorySerializer, self).to_representation(category)
