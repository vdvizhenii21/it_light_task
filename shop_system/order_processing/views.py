from .models import Product, Order, Invoice
from rest_framework import viewsets
from .serializers import ProductSerializer, OrderSerializer, InvoiceSerializer
from .filters import OrderItemFilter
from django_filters import rest_framework as filters
from .permissions import IsAccountant

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filter_class = OrderItemFilter


class InvoiceViewSet(viewsets.ModelViewSet):
    permission_classes = IsAccountant
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

