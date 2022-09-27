from operator import mod
from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=3)
    tital = models.CharField(max_length=20)
    description = models.CharField(max_length=10)

    def __str__(self):
        return self.name

