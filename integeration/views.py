from django.shortcuts import render
from order.models import Txn, Order
from rest_framework.views import APIView

# Create your views here.
# class CreateTxn(APIView):
#     def post(self, request, format=None):
#         webhook_data = request.data

#         request.data.