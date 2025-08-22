from random import choice

from django_filters import rest_framework as django_filters
from .models import Product, Category, FlashSale, Order


class ProductFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    category = django_filters.CharFilter(field_name='category__name', lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['min_price', 'max_price']


class CategoryFilter(django_filters.FilterSet):
    class Meta:
        model = Category
        fields = ['name']


class FlashSaleFilter(django_filters.FilterSet):
    min_discount_percentage = django_filters.NumberFilter(field_name='discount_percentage', lookup_expr='gte')
    max_discount_percentage = django_filters.NumberFilter(field_name='discount_percentage', lookup_expr='lte')
    product = django_filters.CharFilter(field_name='product__title', lookup_expr='icontains')

    class Meta:
        model = FlashSale
        fields = ['min_discount_percentage', 'max_discount_percentage', 'product']

# class OrderFilter(django_filters.FilterSet):
#     status = django_filters.CharFilter(choices=Order.STATUS)
#     start_date = django_filters.DateFilter(field_name="created_at", lookup_expr="gte")
#     end_date = django_filters.DateFilter(field_name="created_at", lookup_expr="lte")
#     user = django_filters.NumberFilter(field_name="user__id")
#     product = django_filters.CharFilter(field_name="items__product__title", lookup_expr="icontains")
#     min_total = django_filters.NumberFilter(field_name="total_price", lookup_expr="gte")
#     max_total = django_filters.NumberFilter(field_name="total_price", lookup_expr="lte")
#
#     class Meta:
#         model = Order
#         fields = ['status', 'user', 'product', 'start_date', 'end_date', 'min_total', 'max_total']
