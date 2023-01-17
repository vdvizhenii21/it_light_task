import django_filters
from django_filters import DateFromToRangeFilter
from .models import Order


class OrderItemFilter(django_filters.FilterSet):
    create_date = DateFromToRangeFilter()

    class Meta:
        model = Order
        fields = ['create_date']
