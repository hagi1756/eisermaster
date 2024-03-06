from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class Myuser(AbstractUser):
    phone = models.CharField(max_length = 15, null=True, blank=True)
    address = models.CharField(max_length = 255, null=True, blank=True)
    country = models.CharField(max_length = 100, null=True, blank=True)
    city = models.CharField(max_length = 100, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)