from django.contrib import admin
from .models import GreenieUser, DeleveryAddress


# Register your models here.
@admin.register(GreenieUser)
class GreenieUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'active', 'gender', 'created', 'modified')
    ordering = ['-modified']


@admin.register(DeleveryAddress)
class DeleveryAddressAdmin(admin.ModelAdmin):
    list_display = ('city', 'state', 'pincode', 'phone', 'is_active', 'type', 'created', 'modified')
    ordering = ['-modified']