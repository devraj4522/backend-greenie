from rest_framework import routers
from django.urls import path, include

from . import views

router = routers.SimpleRouter()
# router.register(r'', views.UserViewSet)
# router.register(r'', views.ContactViewSet)

urlpatterns = [
    path('user-account/', views.UserView.as_view(), name='user-login-signup'),
    path('user-address/<str:id>', views.AddressView.as_view(), name='user-address'),
    path('user-address-list', views.AddressListView.as_view(), name='user-address-list'),
    path('create-address/', views.CreateAddress.as_view(), name='create-address'),
    path("test/", views.TestView.as_view(), name="test"),
    path('', include(router.urls))
]
