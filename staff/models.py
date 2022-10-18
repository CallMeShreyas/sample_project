from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Staff(models.Model):
    name = models.CharField(max_length = 20)
    surname = models.CharField(max_length = 20)
    user_name = models.CharField(max_length = 10)
    password = models.CharField(max_length = 10)
    disabled = models.BooleanField(default = False)

    def __str__(self):
        return self.name
