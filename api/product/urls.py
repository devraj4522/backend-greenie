from rest_framework import routers
from django.urls import path, include

from . import views

router = routers.DefaultRouter()
router.register(r'', views.ProductViewSet)
router.register(r'category/(?P<category>\w+)', views.ProductbyCategoryViewSet)
router.register(r'review/(?P<product>\d+)', views.ReviewViewSet)

urlpatterns = [
    path('review/add/<str:product_id>/<str:token>/',
         views.add, name='product.add'),
    path('', include(router.urls))
]
