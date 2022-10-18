from django.db import models

# Create your models here.

class Student(models.Model):
    rollno = models.IntegerField(null = False, default = 0)
    name = models.CharField(max_length = 20)
    surname = models.CharField(max_length = 20)
    user_name = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)
    disabled = models.BooleanField(default = False)

    def __str__(self):
        return self.name