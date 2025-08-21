from django.db import models
from ..models import Product
from django.utils.timezone import now


class FlashSale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    discount_percentage = models.PositiveIntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def is_active(self):
        return self.start_time <= now() <= self.end_time

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['product', 'start_time', 'end_time'], name='unique_flashsale_period')
        ]
