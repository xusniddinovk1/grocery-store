from users.models import CustomUser
from .product import Product
from django.db import models


class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'product']

    def __str__(self):
        return f'{self.product.title} commented by {self.user.username}'
