from django.db import models
import uuid


# Create your models here.
class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=156)
    description = models.CharField(max_length=1000)
