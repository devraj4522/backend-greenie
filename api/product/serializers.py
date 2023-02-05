from dataclasses import fields
import email
from pyexpat import model
from unicodedata import category
from rest_framework import serializers
from .models import Product, Review
from api.user_app.models import CustomUser


class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(
        max_length=None, allow_empty_file=False, allow_null=True, required=False)
    category = serializers.StringRelatedField(many=False)

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'image', 'category')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('name', 'email', 'image')


class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    product = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Review
        fields = ('id', 'title', 'description', 'product',
                  'user', 'rating', 'created', 'updated')
