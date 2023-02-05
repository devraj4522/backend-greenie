from .serializers import OrderSerializer
from .models import Order
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from user.permissions import IsAdminUser
from rest_framework.views import APIView
from backend_greenie.utils.response_formatting import FormattedResponse
from .model_helpers import StatusType
from user.models import DeleveryAddress
from django.core.exceptions import ObjectDoesNotExist
from product.models import Product
from django.db.models import Q
from django.db.models import Prefetch

from integeration.braintree.braintree_main import BrainTreeMain
bt = BrainTreeMain()
token = bt.gateway.client_token.generate()
# print(token)
class OrderListView(ListAPIView):
    """
    List of orders.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )

    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['id','user','product__name', 'product__category__name', 'status']
    search_fields = ['user__name', 'product__name', 'product__category__name']

    page_size = 20

    def get_queryset(self):
        user = self.request.user
        greenie_user = user.greenie_user

        if self.request.query_params.get('status', None):
            status_vals = self.request.query_params.get('status').split(',')
            orders = Order.objects.filter(status__in = status_vals, user=greenie_user).order_by('-modified')
        else :
            orders = Order.objects.filter(is_active=True).order_by('-modified')

        return orders

    def list(self, request, *args, **kwargs):
        # call the original 'list' to get the original response
        response = super(OrderListView, self).list(request, *args, **kwargs)

        return FormattedResponse(response.data)

class OrderDetailView(RetrieveAPIView):
    """
        Order detail: Single object
    """
    uthentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )
    queryset = Order.objects.filter(is_active=True)
    serializer_class = OrderSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        data =  super(OrderDetailView, self).get(request, *args, **kwargs)
        return FormattedResponse(msg='Order Data Fetch successully.', data=data.data).create()

class CartView(APIView):
    """
    Add to card.
    Remove From Cart
    Get Cart Items.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )

    def post(self, request, format=None):
        user = request.user
        greenie_user = user.greenie_user
        product = request.data['product_id']
        keep_in_cart = request.data['is_add'] # add or remove item from cart
        if keep_in_cart:
            Order.objects.create(user=greenie_user, product__id=product, status=StatusType.ADDED_TO_CART)
            query_data = Order.objects.filter(user=greenie_user, is_active=True, status=StatusType.ADDED_TO_CART)
            response_data = OrderSerializer(query_data, many=True)
            return FormattedResponse(msg='Added to Cart Successfully.', data=response_data).create()
        else:
            orders = Order.objects.filter(user=greenie_user, is_active=True, status=StatusType.ADDED_TO_CART)
            current_product_in_cart = orders.filter(product__id=product)
            if len(current_product_in_cart):
                order = current_product_in_cart.latest('modified')
                order.status = StatusType.VIEWED
                order.save()
                orders.remove(order)
            response_data = OrderSerializer(orders, many=True)
            return FormattedResponse(msg='Removed from cart', data=response_data).create()

    def get(self, request, format=None):
        user = request.user
        greenie_user = user.greenie_user
        query_data = Order.objects.filter(user=greenie_user, is_active=True, status=StatusType.ADDED_TO_CART)
        response_data = OrderSerializer(query_data, many=True)
        return FormattedResponse(msg='Added to Cart Successfully.', data=response_data).create()

class CreateOrderView(APIView):
    """
    create an order.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )

    def post(self, request, format=None):
        user = request.user
        greenie_user = user.greenie_user
        # body : {"products": {"id1": 2, "id2": 3}}
        is_order_through_cart = request.data['is_order_through_cart']
        address = request.data['address_id']
        
        try:
            address_obj = DeleveryAddress.objects.get(id =address)
        except ObjectDoesNotExist:
            return FormattedResponse(error=True, msg='First Add Delevery Address.').create()

        if not is_order_through_cart:
            products = request.data['products']
            products_query = Product.objects.filter(id__in=products.keys())
            if len(products_query) != len(products):
                return FormattedResponse(error=True, msg="All Product must exist.").create()

            for product in products_query:
                for _ in range(products[product]):
                    order_obj = Order.objects.create(user=greenie_user, product=product, status = StatusType.PAYMENT_PENDING)
        else:
            orders = Order.objects.filter(user=greenie_user, status=StatusType.ADDED_TO_CART, is_active=True)
            for order in orders:
                order.status = StatusType.PAYMENT_PENDING
                order.save()
        
        # TODO: First get payment 
        # Create Txn 
        # Mark order completed
        orders = Order.objects.filter(user=greenie_user, status=StatusType.PAYMENT_PENDING, is_active=True)
        response_data = OrderSerializer(orders, many=True).data
        return FormattedResponse(msg='Orders Awaiting payment.', data=response_data).create()