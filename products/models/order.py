from django.db import models
from django.core.validators import RegexValidator

from products.models import Product
from users.models import CustomUser

phone_regex = RegexValidator(
    regex=r'^\+998\d{9}$',
    message='Phone number must be the following: +998 xx xxx xx xx'
)


class Order(models.Model):
    PENDING = 'Pending'
    PROCESSING = 'Processing'
    SHIPPED = "Shipped"
    DELIVERED = 'Delivered'
    CANCELED = 'Canceled'

    STATUS = (
        (PENDING, 'Pending'),
        (PROCESSING, 'Processing'),
        (SHIPPED, "Shipped"),
        (DELIVERED, 'Delivered'),
        (CANCELED, 'Canceled')
    )

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    phone_number = models.CharField(validators=[phone_regex], unique=True)
    status = models.CharField(max_length=20, choices=STATUS, default=PENDING)
    is_paid = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def set_status(self, new_status):
        if new_status not in dict(self.STATUS):
            raise ValueError('Invalid Error')
        self.status = new_status
        self.save()

    def is_transition_allowed(self, new_status):
        allowed_transition = {
            self.PENDING: [self.PROCESSING, self.CANCELED],
            self.PROCESSING: [self.SHIPPED, self.CANCELED],
            self.SHIPPED: [self.DELIVERED, self.CANCELED],
        }
        return new_status in allowed_transition.get(self.status, [])

    def get_total(self):
        return sum(item.get_total() for item in self.items.all())

    def __str__(self):
        return f'Order #{self.id} by {self.user}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # qo‘shildi

    def save(self, *args, **kwargs):
        if not self.price:  # yangi yaratilganda
            self.price = self.product.get_discounted_price()
        super().save(*args, **kwargs)

    def get_total(self):
        return self.price * self.quantity

    def __str__(self):
        return f'{self.product.title} x {self.quantity}'
