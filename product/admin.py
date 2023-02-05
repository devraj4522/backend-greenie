from django.contrib import admin

# Register your models here.
from .models import Product, Review, Category


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'stock', 'is_active', 'created', 'modified')
    ordering = ['-modified']

@admin.register(Review)
class ReviewtAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'rating', 'product', 'user', 'is_active')
    ordering = ['-modified']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'active')
    ordering = ['-modified']
