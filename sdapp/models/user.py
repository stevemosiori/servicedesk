from django.db import models
from django.contrib.auth.models import User

class AppUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    timezone = models.CharField(max_length=191, blank=True, null=True)
    gender = models.CharField(max_length=191, blank=True, null=True)
    timeformat = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        db_table = 'users'

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    timezone = models.CharField(max_length=191, blank=True, null=True)
    timeformat = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        db_table = 'customers'