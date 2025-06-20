from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])

class Product(models.Model):
    category = models.ForeignKey(
        Category,
        related_name='products',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Price in your local currency"
    )
    contact_phone = models.CharField(
        max_length=20,
        help_text="Phone number for buyers to contact"
    )
    location = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Where the product is located"
    )
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        upload_to='products/%Y/%m/%d',
        blank=True,
        null=True
    )
    
    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created']),
            models.Index(fields=['slug']),
        ]
    
    def __str__(self):
        return f"{self.name} (${self.price})"
    
    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)