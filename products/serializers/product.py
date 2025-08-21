from rest_framework import serializers
from ..models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class ProductSerializer(serializers.ModelSerializer):
    discounted_price = serializers.SerializerMethodField()
    flash_sale_active = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'category', 'price', 'flash_sale_active','discounted_price','stock', 'created_at']

    def get_discounted_price(self, obj):
        return obj.get_discounted_price()

    def get_flash_sale_active(self, obj):
        return bool(obj.get_active_flash_sale())
