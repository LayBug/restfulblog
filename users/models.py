from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass


class UserProfile(models.Model):
    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    first_name = models.CharField(max_length = 15)
    last_name = models.CharField(max_length = 15)
    email = models.EmailField()


