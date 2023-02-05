from rest_framework import serializers

from .models import Order, Txn

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        depth=1
        fields = '__all__'

class TxnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Txn
        fields = '__all__'
