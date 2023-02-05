from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
# from .serializers import UserSerializer, ContactSerializer
# from .models import  Contact
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout
import random
import re
from integeration.signal import test_signal
from rest_framework.views import APIView
from rest_framework.response import Response

def generate_session_token(length=10):
    return ''.join(random.SystemRandom().choice([chr(i) for i in range(97, 123)] + [str(i) for i in range(10)]) for _ in range(length))


@csrf_exempt
def signin(request):
    if not request.method == 'POST':
        return JsonResponse({'error': 'Send a post request with valid paramenter only'})

    # print(request.POST.get('email', None))  - if you will not get email, None will be printed
    username = request.body['email']
    password = request.body['password']

    print(username)
    print(password)

    # validation part
    if not re.match("^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", username):
        return JsonResponse({'error': 'Enter a valid email'})

    if len(password) < 3:
        return JsonResponse({'error': 'Password needs to be at least of 3 char'})

    UserModel = get_user_model()

    try:
        user = UserModel.objects.get(email=username)

        if user.check_password(password):
            usr_dict = UserModel.objects.filter(
                email=username).values().first()
            usr_dict.pop('password')

            if user.session_token != "0":
                user.session_token = "0"
                user.save()
                return JsonResponse({'error': "Previous session exists!"})

            token = generate_session_token()
            user.session_token = token
            user.save()
            login(request, user)
            test_signal.send(sender=__name__, a= 1)
            return JsonResponse({'token': token, 'user': usr_dict})
        else:
            return JsonResponse({'error': 'Invalid password'})

    except UserModel.DoesNotExist:
        return JsonResponse({'error': 'Invalid Email'})


def signout(request, id):
    logout(request)

    UserModel = get_user_model()

    try:
        user = UserModel.objects.get(pk=id)
        user.session_token = "0"
        user.save()

    except UserModel.DoesNotExist:
        return JsonResponse({'error': 'Invalid user ID'})

    return JsonResponse({'success': 'Logout success'})


# class UserViewSet(viewsets.ModelViewSet):
#     authentication_classes = []
#     permission_classes = []
#     # ... rest of the viewse
#     permission_classes_by_action = {'create': [AllowAny]}

#     # queryset = CustomUser.objects.all().order_by('id')
#     serializer_class = UserSerializer

#     def get_permissions(self):
#         try:
#             return [permission() for permission in self.permission_classes_by_action[self.action]]

#         except KeyError:
#             return [permission() for permission in self.permission_classes]


# class ContactViewSet(viewsets.ModelViewSet):
#     permission_classes_by_action = {'create': [IsAuthenticated]}

#     queryset = Contact.objects.all().order_by('id')
#     serializer_class = ContactSerializer

#     def get_permissions(self):
#         try:
#             return [permission() for permission in self.permission_classes_by_action[self.action]]

#         except KeyError:
#             return [permission() for permission in self.permission_classes]


class TestView(APIView):
    permission_classes = []
    authentication_classes = []

    def get(self, request, format=None):
        return Response({'info': 'Django ReactAPI', 'name': "Dev Raj Singh"})