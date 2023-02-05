from rest_framework import serializers
from .models import GreenieUser, DeleveryAddress


class GreenieUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = GreenieUser
        depth = 1
        fields = 'id', 'name', 'phone', 'active', 'email', 'images', 'gender'


class DeleveryAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeleveryAddress
        fields = '__all__'
