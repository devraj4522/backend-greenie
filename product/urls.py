from rest_framework import routers
from django.urls import path, include

from . import views

router = routers.SimpleRouter()

router.register('review', views.ReviewViewSet)
router.register('category', views.CategoryViewSet)
router.register(r'', views.ProductViewSet)

# router.register(r'review/(?P<product>\d+)', views.ReviewViewSet)

urlpatterns = [
    # path('review/add/<str:product_id>/<str:token>/',
    #      views.add, name='product.add'),
     path('product-list/', views.ProductListViewSet.as_view(), name='product-list'),
    path('', include(router.urls)),
    
]
