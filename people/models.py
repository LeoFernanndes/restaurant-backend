from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Customer(User):
    cpf = models.CharField(max_length=11)
