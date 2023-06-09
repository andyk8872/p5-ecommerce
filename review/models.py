from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from products.models import Product


class Review(models.Model):
    """  Review Model """

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True, null=True)

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=True,
        related_name='p_review',
    )

    review = models.TextField(max_length=200, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering: ['-created_on',]

    def __str__(self):
        return f"Review {self.review} by {self.user}."
