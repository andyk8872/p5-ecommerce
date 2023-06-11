from django.db import models

# Create your models here.


class Contact(models.Model):
    """Model for contact form"""
    CONTACT_OPTIONS = [
        ('general', 'General Enquiry'),
        ('product', 'product'),
        ('sales', 'Sales'),
        ('other', 'Other'),
    ]
    email = models.EmailField(
        max_length=254,
        null=False,
        blank=False
    )
    message = models.TextField(max_length=700)
    subject = models.CharField(max_length=15, choices=CONTACT_OPTIONS)
    created_on = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.email
