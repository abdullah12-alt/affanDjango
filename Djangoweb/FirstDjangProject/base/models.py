from django.db import models

# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length=200)
    Email= models.EmailField(max_length=200)