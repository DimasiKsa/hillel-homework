import uuid
from django.core.validators import MinLengthValidator
from django.db import models
import datetime
from faker import Faker
from students.validators import no_elon_validator
from courses.models import Course


class Person(models.Model):

    first_name = models.CharField(
        max_length=60, null=False, validators=[MinLengthValidator(2)]
    )
    last_name = models.CharField(
        max_length=80, null=False, validators=[MinLengthValidator(2)]
    )
    email = models.EmailField(
        max_length=120, null=True, validators=[no_elon_validator], unique=True
    )
    birthdate = models.DateField(null=True, default=datetime.date.today)

    avatar_image = models.ImageField(upload_to='static/', null=True, blank=True)

    summary = models.FileField(upload_to='static/', null=True, blank=True)

    class Meta:
        abstract = True


class Student(Person):

    course = models.ForeignKey(Course, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.full_name()}, {self.age()}, {self.email} id({self.id})"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def age(self):
        return datetime.datetime.now().year - self.birthdate.year

    @classmethod
    def generate_instances(cls, count):
        faker = Faker()
        for _ in range(count):
            st = cls(
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                email=faker.email(),
                birthdate=faker.date_time_between(start_date="-30y", end_date="-18y"),
            )
            st.save()

