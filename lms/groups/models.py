from django.db import models

# Create your models here.

class Groups(models.Model):
    first_name = models.CharField(max_length=60, null=False)
    last_name = models.CharField(max_length=80, null=False)
    group_name = models.CharField(max_length=20, null=False)