from django.db import models
from people.models import User


class Address(models.Model):
    street = models.CharField(max_length=255)
    number = models.CharField(max_length=10)
    complement = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=11)
    neighbourhood = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)


class PersonAddress(Address):
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    is_default = models.BooleanField(default=True)