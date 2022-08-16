from itertools import product
from keyword import kwlist
from turtle import st
from unicodedata import category
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from api.category.models import Category

from .serializers import ProductSerializer, ReviewSerializer
from .models import Product, Review
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Show prodcuts and filter on the basis of index


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer


class ProductbyCategoryViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer

    def get_queryset(self):
        try:
            category_name = self.kwargs.get('category')
            cat = Category.objects.get(name=category_name)
            self.queryset = self.queryset.filter(category=cat)
            return self.queryset
        except:
            return self.queryset.filter(category=-1)


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer

    queryset = Review.objects.all().order_by('id')

    def get_queryset(self):
        product = self.kwargs.get('product')
        if product:
            self.queryset = self.queryset.filter(product=product)
        return self.queryset


def validate_user_session(id, token):
    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(pk=id)
        if user.session_token == token:
            return True
        return False
    except UserModel.DoesNotExist:
        return False


# Add review
@csrf_exempt
def add(request, product_id, token):
    if request.method == "POST":
        user = request.POST['user']
        rating = request.POST['rating']
        title = request.POST['title']
        description = request.POST['description']

        if not validate_user_session(user, token):
            return JsonResponse({'error': 'Please re-login', 'code': '1'})

        UserModel = get_user_model()

        product = Product.objects.get(pk=product_id)

        if not product:
            return JsonResponse({"error": "Product Not Found"})

        try:
            user = UserModel.objects.get(pk=user)
        except UserModel.DoesNotExist:
            return JsonResponse({'error': 'User does not exist'})

        try:
            review = Review(user=user, product=product, title=title,
                            description=description, rating=rating)
            review.save()
        except UserModel.DoesNotExist:
            return JsonResponse({'error': 'Not Able to Add Review'})

        return JsonResponse({'success': True, 'error': False, 'msg': 'Review Added Successfully'})
