# customer360/models.py

from django.db import models

class Customer(models.Model):
    # Fields for the Customer model
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    social_media = models.CharField(max_length=100, blank=True)  # New field added

    def __str__(self):
        return str(self.id)

class Interaction(models.Model):
    # Choices for channel and direction fields
    CHANNEL_CHOICES = [
        ('phone', 'Phone'),
        ('sms', 'SMS'),
        ('email', 'Email'),
        ('letter', 'Letter'),
        ('social_media', 'Social Media'),  # New interaction channel added
    ]

    DIRECTION_CHOICES = [
        ('inbound', 'Inbound'),
        ('outbound', 'Outbound'),
    ]

    # Fields for the Interaction model
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    channel = models.CharField(max_length=15, choices=CHANNEL_CHOICES)
    direction = models.CharField(max_length=10, choices=DIRECTION_CHOICES)
    interaction_date = models.DateField(auto_now_add=True)
    summary = models.TextField()
