from django.db import models

# Create your models here.
class SMS(models.Model):
    content = models.TextField()