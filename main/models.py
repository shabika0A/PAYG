from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager as DefaultUserManager


class customUser(DefaultUserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        # extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('reqcount', 0)
        return self._create_user(username, email, password, **extra_fields)

class User(AbstractUser):

    reqcount = models.PositiveIntegerField(default=0)
    objects = customUser()
