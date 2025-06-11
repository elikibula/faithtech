# models.py
from django.db import models

class Device(models.Model):
    DEVICE_TYPES = [
        ('Laptop', 'Laptop'),
        ('Phone', 'Phone'),
        ('Others', 'Others')
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100, blank=True)
    device_type = models.CharField(max_length=10, choices=DEVICE_TYPES)
    other_device_type = models.CharField(max_length=100, blank=True)
    brand = models.CharField(max_length=50, blank=True)
    model = models.CharField(max_length=100, blank=True)
    issue_description = models.TextField(blank=True)
    resolve_description = models.TextField(blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending', blank=True)
    date_received = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.device_type})"