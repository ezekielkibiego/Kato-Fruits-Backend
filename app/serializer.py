from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name')
    category_slug = serializers.CharField(source='category.slug')
    category_id = serializers.IntegerField(source='category.id')
    class Meta:
        model = Product
        fields = ['id', 'name', 'slug', 'image1', 'image2', 'image3', 'description','new_price', 'old_price', 'is_available','category_name','get_url','category_slug','category_id']

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'products']