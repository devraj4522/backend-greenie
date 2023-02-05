from rest_framework import routers
from django.urls import path, include

from . import views

router = routers.SimpleRouter()
# router.register(r'', views.UserViewSet)
# router.register(r'', views.ContactViewSet)

urlpatterns = [
    path('create-order/', views.CreateOrderView.as_view(), name='create-order'),
    path('order-list/', views.OrderListView.as_view(), name='order-list'),
    path('order-detail/<str:id>', views.OrderDetailView.as_view(), name='order-detail'),
    path('cart/', views.CartView.as_view(), name='cart-detail'),
    # path("test/", views.TestView.as_view(), name="test"),
    path('', include(router.urls))
]
