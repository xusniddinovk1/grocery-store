from rest_framework import serializers
from ..models import Order, OrderItem, Product


class OrderItemSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    total_price = serializers.SerializerMethodField()
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Order
        fields = ['id', 'user', 'phone_number', 'items', 'total_price', 'is_paid', 'created_at']
        read_only_fields = ['user', 'total_price', 'created_at']

    def get_total_price(self, obj):
        return sum([item.product.price * item.quantity for item in obj.items.all()])

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        user = self.context['request'].user
        order = Order.objects.create(user=user, **validated_data)

        for item_data in items_data:
            product = item_data['product']
            quantity = item_data['quantity']

            if not Product.objects.filter(pk=product.pk).exists():
                raise serializers.ValidationError({'product': f'Product with id {product.pk} does not exist'})

            if product.stock < quantity:
                raise serializers.ValidationError(
                    {'product': f'Product {product.title} has only {product.stock} in stock'})

            OrderItem.objects.create(order=order, product=product, quantity=quantity)
            product.stock -= quantity
            product.save()

        return order
