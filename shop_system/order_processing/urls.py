from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, OrderViewSet, InvoiceViewSet

router_v1 = DefaultRouter()

router_v1.register('products', ProductViewSet, basename='products')
router_v1.register('order', OrderViewSet, basename='order')
router_v1.register('invoice', InvoiceViewSet, basename='invoice')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]