from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class VarsayılanKullanıcı(AbstractUser):
    unvan = models.TextField(max_length=30)