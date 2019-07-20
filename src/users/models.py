from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=99)
    last_name = models.CharField(max_length=99)
    location = models.CharField(max_length=99, blank=True)
    image = models.ImageField(default='profile.jpg', upload_to='profile_pics')
    
    def __str__(self):
        return f'{ self.user.username }  Profile'
