from django.shortcuts import render
from rest_framework.views import APIView
from integeration.braintree.braintree_main import BrainTreeMain
from integeration.braintree.braintree_wrapper import BrainTreeWrapper
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from backend_greenie.utils.response_formatting import FormattedResponse
from order.models import Order, Purchase, Txn
from order.model_helpers import StatusType, TxnType
from django.db.models import Sum
from user.models import DeleveryAddress
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime
from order.serializers import TxnSerializer

# Create your views here.
class SendPaymentToken(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )
    
    def get(self, request, format=None):
        braintree = BrainTreeMain()
        response_data = braintree.generate_token()
        return FormattedResponse(msg="Token Generated.", data=response_data).create()

class MakePayment(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )
    
    def post(self, request, format=None):
        paymentMethodNonce = self.request.data['paymentMethodNonce']
        amount = request.data['amount']
        products= request.data['products']
        address = request.data['address_id']
        # print(paymentMethodNonce, amount, products)
        user = request.user
        try:
            greenie_user = user.greenie_user
        except:
            return FormattedResponse(error=True, msg="User not exists.", data={}).create()

        try:
            address_obj = DeleveryAddress.objects.get(id=address)
        except ObjectDoesNotExist:
            return FormattedResponse(error=True, msg="Address not exists.", data={}).create()

        orders = Order.objects.filter(user= greenie_user, status=StatusType.PAYMENT_PENDING, is_active=True, product__id__in=products)
        print(orders)
        actual_price_sum = orders.aggregate(total=Sum('product__price'))['total']
        print(actual_price_sum)
        if actual_price_sum != amount:
            return FormattedResponse(error=True, msg="Total amount is not equal to order amount.", data={}).create()

        # make payment        
        braintree_wrapper = BrainTreeWrapper()
        res = braintree_wrapper.make_payment(paymentMethodNonce, amount)
        if res['error']:
            return FormattedResponse(error=True, msg="Error Occured in making payment", data={}).create()
        
        response_data = res['transaction']
        
        #mark payment done
        for order in orders:
            order.status = StatusType.PAYMENT_DONE
            order.save()
        
        # create a purchase under which all order will go
        purchase = Purchase.objects.create(address=address_obj, user=user)
        today = datetime.now().date()
        txns = []
        for order in orders:
            txn = Txn.objects.create(user=user, type=TxnType.CREDIT, product=order.product, amt=order.product.price, txn_date=today, note="", order=order, purchase=purchase)
            txns.append(txn)
        txn_response_data = TxnSerializer(txns, many=True).data
        response_data['txns'] = txn_response_data
        return FormattedResponse(msg="Payment Successful", data=response_data).create()