from rest_framework import serializers
from .models import Product, Order, Invoice


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Product


class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    class Meta:
        fields = '__all__'
        model = Order


class InvoiceSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Invoice
