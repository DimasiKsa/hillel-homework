from django.shortcuts import render
from django.http import HttpResponse
from students.models import Student
from students.utils import format_records
from webargs.djangoparser import use_kwargs, use_args
from webargs import fields



def hello_students(request):
    return HttpResponse('SUCCESS')


@use_kwargs(
    {
        "first_name": fields.Str(
            required=False,
            missing=None,
        ),
        "last_name": fields.Str(
            required=False,
            missing=None,
        ),
    },
    location="query",
)
def get_students(request, first_name, last_name):

    students = Student.objects.all()
    if first_name:
        students = students.filter(first_name=first_name)
    if last_name:
        students = students.filter(last_name=last_name)
    result = format_records(students)
    return HttpResponse(result)

