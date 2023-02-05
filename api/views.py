from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.


class HomeView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        return Response({'info': 'Django ReactAPI', 'name': "Dev Raj Singh"})
