import uuid
import datetime
from django.db import models

# Create your models here.


class Course(models.Model):

    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)

    name = models.CharField(null=False, max_length=120)

    start_date = models.DateField(null=True, default=datetime.date.today)

    count_of_students = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}"


class UserType(models.Model):

    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)

    name = models.CharField(null=False, max_length=120)

    def __str__(self):
        return f"{self.name}"