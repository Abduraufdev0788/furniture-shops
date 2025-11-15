from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=30, unique=True)
    last_name = models.CharField(max_length=30, unique=True)
    tel = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=128, unique=True)
    confirm_password = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, default='avatar/default.png', null=True)
 
    def __str__(self):
        return f"Profile of {self.user.first_name}"