from django.db import models
from seller.models import Seller

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('divan', 'Divanlar'),
        ('krovat', 'Krovatlar'),
        ('stol', 'Stollar'),
        ('shkaf', 'Shkaflar'),
        ('yotoqxona', 'Yotoqxona Mebellari'),
    ]
    seller_product = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=14, decimal_places=2)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='products/', default='products/default.png')
    created_at = models.DateTimeField(auto_now_add=True)
    
    

    def __str__(self):
        return self.name