from django.core.management.base import BaseCommand
from order_processing.models import Product
import datetime
from django.utils import timezone



class Command(BaseCommand):
    def handle(self, *args, **options):
        for product in Product.objects.all():
            if (datetime.date.today() - product.create_date.date()).days >= 31 and product.discount_activate == False:
                product.discount_activate = True
                product.price = int(product.price * (100 - 20) / 100)
                product.save()
