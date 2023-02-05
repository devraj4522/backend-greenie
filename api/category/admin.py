from django.contrib import admin
from .models import Category
# Register your models here.

# @admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
#     # ordering = ['-updated_at']
    list_display = ('name', )
#     # list_display = ('id','name','updated_at','created_at',)
#     # list_display = ('id','comment','user','tab','created','financerequest','financerequests')

admin.site.register(Category, CategoryAdmin)
