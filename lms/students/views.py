from django.shortcuts import render
from django.http import HttpResponse
from students.models import Student
from students.utils import format_records
from webargs.djangoparser import use_kwargs, use_args
from webargs import fields



def hello_students(request):
    return HttpResponse('SUCCESS')


@use_args(
    {
        "first_name": fields.Str(
            required=False,

        ),
        "last_name": fields.Str(
            required=False,

        ),
    },
    location="query",
)
def get_students(request, params):

    students = Student.objects.all()
    for param_name, param_val in params.items():
        students = students.filter(**{param_name: param_val})

    result = format_records(students)

    return HttpResponse(result)

