from rest_framework import routers
from django.urls import path, include

from . import views

router = routers.SimpleRouter()

urlpatterns = [
    path('gettoken/', views.SendPaymentToken.as_view(), name='get-payment-token'),
    path('makepayment/', views.MakePayment.as_view(), name='make-payment'),
    # path("test/", views.TestView.as_view(), name="test"),
    path('', include(router.urls))
]
