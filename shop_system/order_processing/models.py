from django.db import models
from django.core.validators import MinValueValidator


class Status(models.TextChoices):
    NEW = 'new'
    DONE = 'done'
    PAID = 'paid'


class Product(models.Model):
    name = models.CharField(db_index=True,
                            max_length=200,
                            verbose_name='product name')
    price = models.IntegerField(
        verbose_name='price of product',
        validators=[MinValueValidator(1)]
    )
    discount_activate = models.BooleanField(default=False)
    create_date = models.DateTimeField(verbose_name='creation date',
                                       auto_now_add=True,
                                       db_index=True)


class Order(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='product of order',
        related_name='order_product'
    )
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.NEW,
    )
    create_date = models.DateField(verbose_name='creation date',
                                       auto_now_add=True,
                                       db_index=True)


class Invoice(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        verbose_name='invoice of order',
        related_name='invoice_order'
    )
    create_date = models.DateTimeField(verbose_name='creation date',
                                       auto_now_add=True,
                                       db_index=True)
