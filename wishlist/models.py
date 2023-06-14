from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from products.models import Product


class Wishlist(models.Model):
    # Model for wishlist
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}: Wish List'
