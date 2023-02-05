from django.urls import path, include
from rest_framework.authtoken import views
from . import views

urlpatterns = [
    # path('test/', views.HomeView.as_view(), name='test'),
    path('category/', include('api.category.urls')),
    path('product/', include('api.product.urls')),
    # path('user/', include('apis.user_app.urls')),
    # path('order/', include('apis.order.urls')),
    # path('payment/', include('apis.payment.urls')),
    # path('api-token-auth/', views.obtain_auth_token, name='api_token_auth'),

]
