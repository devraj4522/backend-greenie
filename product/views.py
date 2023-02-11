from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from .serializers import CategorySerializer, ProductSerializer, ReviewSerializer
from .models import Category, Product, Review
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from user.permissions import IsAdminUser

# Create your views here.


class CategoryViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )
    queryset = Category.objects.filter(active=True).order_by('-modified')
    serializer_class = CategorySerializer

    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['id','name', 'subtitle']
    search_fields = ['name',]
    page_size = 20
    
    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = [IsAdminUser, ]
        return super().get_permissions()


class ProductViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['id','name', 'price', 'stock', 'category']
    search_fields = ['name', 'description']
    page_size = 20

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

    
class ReviewViewSet(viewsets.ModelViewSet):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['title','description', 'rating', 'product__id']
    search_fields = ['title', 'description']
    page_size = 20

    def get_queryset(self):
        return Review.objects.filter(is_active=True)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user.greenie_user)

