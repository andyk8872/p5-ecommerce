from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Review(models.Model):
    user = models.ForeignKey(
                             settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE
                            )
    review = models.TextField(max_length=200, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering: ['-created_on',]

    def __str__(self):
        return f"Review {self.review} by {self.user}."
