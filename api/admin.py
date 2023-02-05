from django.contrib import admin
from api.category.models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ordering = ['-updated_at']
    list_display = ('name', )
