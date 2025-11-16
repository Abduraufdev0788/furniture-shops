from django.db import models

class Seller(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    tel = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=128)
    confirm_password = models.CharField(max_length=128)
    shop_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.shop_name} - {self.first_name} {self.last_name}"
    
