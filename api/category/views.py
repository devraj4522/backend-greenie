from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from .serializers import CategorySerializer
from .models import Category
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


class CategoryViewSet(viewsets.ModelViewSet):
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated, )
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer

    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['id','name']
    search_fields = ['name',]
    page_size = 20
    

