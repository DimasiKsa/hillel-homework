import random
from django.db import models
from faker import Faker

# Create your models here.


class Group(models.Model):
    first_name = models.CharField(max_length=60, null=False)
    last_name = models.CharField(max_length=80, null=False)
    num_group = models.CharField(max_length=5, null=False)

    def __str__(self):
        return f"{self.full_name()}, {self.num_group}, id {self.id}"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @classmethod
    def generate_groups(cls, count):
        faker = Faker()
        for _ in range(count):
            st = cls(
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                num_group=random.randrange(1, 4),
            )
            st.save()
