from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Contacts(models.Model):
    ContactId = models.AutoField(primary_key=True)
    ContactName = models.CharField(max_length=30)
    ContactPhone= models.CharField(max_length=15)
    ContactAddress=models.CharField(max_length=40)