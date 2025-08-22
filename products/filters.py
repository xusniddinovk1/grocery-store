from django_filters import rest_framework as django_filters
from .models import Product, Category, FlashSale


class ProductFilter(django_filters.Filter):
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    category = django_filters.CharFilter(field_name='category__name', lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['category', 'min_price', 'max_price']


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
