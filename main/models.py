from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager as DefaultUserManager


class customUser(DefaultUserManager):
    
    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('reqCount', 0)
        extra_fields.setdefault('totalCostt', 0)

        return self._create_user(username, email, password, **extra_fields)

class User(AbstractUser):
    costPerReq = 0.001  
    reqCount = models.PositiveIntegerField(default=0)
    totalCost = models.DecimalField(max_digits=10, decimal_places=3, default=0)
    objects = customUser()

    def save(self, *args, **kwargs):

        
        self.totalCost = User.costPerReq * self.reqCount
        # print("saved")
        super().save(*args, **kwargs)
