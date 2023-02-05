from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
# from .serializers import UserSerializer, ContactSerializer
from .models import  GreenieUser, DeleveryAddress
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout
from django.core.exceptions import ObjectDoesNotExist
import random
import re
from integeration.signal import test_signal
from rest_framework.views import APIView
from rest_framework.response import Response
from backend_greenie.utils.response_formatting import FormattedResponse
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from rest_framework.authtoken.models import Token
from .serializers import GreenieUserSerializer, DeleveryAddressSerializer
from backend_greenie.users.models import User
from .model_helpers import GenderType
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

def generate_session_token(length=10):
    return ''.join(random.SystemRandom().choice([chr(i) for i in range(97, 123)] + [str(i) for i in range(10)]) for _ in range(length))

class TestView(APIView):
    permission_classes = []
    authentication_classes = []

    def get(self, request, format=None):
        return Response({'info': 'Django ReactAPI', 'name': "Dev Raj Singh"})

class UserView(APIView):
    permission_classes = [] #disables permission

    
    def get(self, request, format=None):
        print(self.request.query_params)
        email = self.request.query_params['email']
        password = self.request.query_params['password']

        try:
            user_obj = User.objects.get(email=email)
            if not user_obj.check_password(password):
                return FormattedResponse(error=True, msg='Password does not matches.').create()
            print('user_obj', user_obj)
        except ObjectDoesNotExist:
            return FormattedResponse(error=True, msg='User Does not exists.').create()
        try:
            greenie_user = GreenieUser.objects.get(user=user_obj)
        except ObjectDoesNotExist:
            return FormattedResponse(error=True, msg='Greenie User Does not exists.').create()
        response_data  = {
                    "auth" : {
                        "user": greenie_user.email,
                        "token" : greenie_user.user.auth_token.pk
                    },
                    "user" : GreenieUserSerializer(greenie_user).data
                }
        return FormattedResponse(msg=response_data).create()

    def post(self, request, format=None):
        email = request.data['email']
        name = request.data['name']
        phone = request.data['phone']
        password = request.data['password']
        gender = request.data['gender']
        uploads = request.data.get('uploads', {})
        #check if user exist
        user_obj = User.objects.filter(username=phone).first()
        if not user_obj:
            user_obj = User.objects.create(username=phone, password=password, email=email)
            user_obj.set_password(password)
            user_obj.save()

            # check if greenie user exist
        greenie_user = GreenieUser.objects.filter(user=user_obj).first()
        if not greenie_user:
            greenie_user = GreenieUser.objects.create(user=user_obj, name=name, phone=phone, active=True, email=email, gender=GenderType[gender], images=uploads)
        else:
            return FormattedResponse(error=True, msg='User Already Exists.').create()
        
        response_data  = {
                    "auth" : {
                        "user": greenie_user.phone,
                        "token" : greenie_user.user.auth_token.pk
                    },
                    "user" : GreenieUserSerializer(greenie_user).data
                } 
        return FormattedResponse(msg='User created successfully', data=response_data).create()


class AddressListView(ListAPIView):
    """
    List of addresss of user.
    Create address too.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )
    queryset = DeleveryAddress.objects.filter(is_active=True)
    serializer_class = DeleveryAddressSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['id','city','state', 'pincode']
    search_fields = ['city', 'pincode']
    page_size = 20

    def list(self, request, *args, **kwargs):
            response = super(AddressListView, self).list(request, *args, **kwargs)
            return FormattedResponse(msg='Data Fetch Successful', data=response.data).create()


class AddressView(RetrieveAPIView):
    """
    Address of user: user-address/id.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )
    queryset = DeleveryAddress.objects.filter(is_active=True)
    serializer_class = DeleveryAddressSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['id','city','state', 'pincode']
    search_fields = ['city', 'pincode']
    lookup_field = 'id'
    page_size = 20

    def get(self, request, *args, **kwargs):
        response = super(AddressView, self).get(request, *args, **kwargs)
        return FormattedResponse(msg='Data Fetch Successful', data=response.data).create()

class CreateAddress(APIView):
    """
    Create address for user.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )
    
    def post(self, request, format=None):
        city = request.data['city']
        state = request.data['state']
        address = request.data['address'].lower()
        pincode = request.data['pincode']
        phone = request.data.get('phone')
        type = request.data['type'] 

        user = request.user
        greenie_user = user.greenie_user
        
        if not phone:
            phone = user.username

        address_query = DeleveryAddress.objects.filter(user = greenie_user, city = city, state = state, address = address, pincode = pincode, phone = phone, type = type)

        if len(address_query):
            response_data = DeleveryAddressSerializer(address_query, many=True).data
            return FormattedResponse(error=True, msg='Address Already Exists.', data=response_data).create()

        address_obj = DeleveryAddress.objects.create(user = greenie_user, city = city, state = state, address = address, pincode = pincode, phone = phone, type = type)
        response_data = DeleveryAddressSerializer(address_obj).data
        return FormattedResponse(msg='Address Created Successfully.', data=response_data).create()