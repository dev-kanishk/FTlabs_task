from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator

# Create your models here.
class User(AbstractUser):
    id = models.CharField(primary_key=True ,max_length=9, validators=[MinLengthValidator(9)])
    real_name = models.CharField(max_length = 100)
    tz = models.CharField(max_length = 100, default="Asia/kolkata")

    def __str__(self):
        return self.real_name

