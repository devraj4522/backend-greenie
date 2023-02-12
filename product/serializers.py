from rest_framework import serializers
from .models import Product, Category, Review


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        depth = 1
        fields = ['id','name','description','subtitle', 'images']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'stock', 'is_active', 'images', 'category')


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'title', 'description', 'rating', 'product', 'is_active', 'created', 'modified')

    def to_representation(self, instance):
        data =  super().to_representation(instance)
        data['user'] = {'id': instance.user.id, 'name': instance.user.name, 'images': instance.user.images}
        return data

