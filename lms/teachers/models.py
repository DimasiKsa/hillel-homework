from django.db import models
from students.models import Person
from courses.models import Course


class Teacher(Person):
    course = models.ManyToManyField(Course,
                                    related_name="teachers")

    def __str__(self):
        return f"{self.full_name()} {self.email} ({self.id}), {self.course}"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
