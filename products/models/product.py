from django.db import models
from django.utils.timezone import now


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    price = models.DecimalField(max_digits=5, decimal_places=3)
    stock = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

    def get_price(self):
        flash_sale = self.flashsale_set.filter(
            start_time__lte=now(),
            end_time__gte=now()
        ).first()

        if flash_sale:
            discount = (self.price * flash_sale.discount_percentage) / 100
            return self.price - discount
        return self.price

    def get_active_flash_sale(self):
        return self.flashsale_set.filter(start_time__lte=now(), end_time__gte=now()).first()

    def get_discounted_price(self):
        flash_sale = self.get_active_flash_sale()
        if flash_sale:
            discount = (self.price * flash_sale.discount_percentage) / 100
            return self.price - discount
        return self.price

    def is_in_stock(self):
        return self.stock > 0

    def increase_stock(self, amount):
        self.stock += amount
        self.save()
        return True

    def reduce_stock(self, quantity):
        if self.stock < quantity:
            return False

        self.stock -= quantity
        self.save()
        return True
