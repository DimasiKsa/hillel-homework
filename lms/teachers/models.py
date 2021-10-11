from django.db import models
# Create your models here.

class Teachers(models.Model):
    first_name = models.CharField(max_length=60, null=False)
    last_name = models.CharField(max_length=80, null=False)
    email = models.EmailField(max_length=120, null=True)
