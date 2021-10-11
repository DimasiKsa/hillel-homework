from django.db import models
import datetime
# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=60, null=False)
    last_name = models.CharField(max_length=80, null=False)
    email = models.EmailField(max_length=120, null=True)
    birthdate = models.DateField(null=True, default=datetime.date.today)