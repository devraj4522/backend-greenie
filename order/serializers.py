from rest_framework import serializers
from product.models import Product
from .models import Order, Txn
from django.core.exceptions import ObjectDoesNotExist

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("id", "user", "product", "status", "is_active")
   
    def to_representation(self, instance):
        data = super().to_representation(instance)
        try:
            print(data)
            data['product'] = {"id": instance.product.id, "name": instance.product.name, "images": instance.product.images, "price": instance.product.price}
        except ObjectDoesNotExist:
            pass
        return data
        
class TxnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Txn
        fields = '__all__'
