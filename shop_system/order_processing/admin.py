from django.contrib import admin
from .models import Product, Order, Invoice


class OrderAdmin(admin.ModelAdmin):
    search_fields = ['create_date']


admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Invoice)

