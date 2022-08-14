from django.db import models
from django.contrib.auth.models import AbstractUser


ROLES = (
    ("super_admin", "super_admin"),
    ("admin", "admin"),
    ("restaurant_admin", "restaurant_admin"),
    ("customer", "customer")
)

class User(AbstractUser):
    cpf = models.CharField(max_length=11)
    role = models.CharField(max_length=30, choices=ROLES, default="customer")

