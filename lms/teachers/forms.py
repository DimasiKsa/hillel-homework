from django.forms import ModelForm
from teachers.models import Teacher
from students.forms import StudentCreateForm
from django.forms import DateInput


class TeacherBaseForm(StudentCreateForm):
    class Meta:
        model = Teacher
        fields = [
            "first_name",
            "last_name",
            "email",
            "birthdate",
            "course"
        ]
        birthdate = {"birthdate": DateInput()}
