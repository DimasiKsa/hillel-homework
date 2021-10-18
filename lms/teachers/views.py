from django.shortcuts import render
from teachers.models import Teacher
from teachers.utils import format_records
from django.http import HttpResponse
# Create your views here.
from webargs.djangoparser import use_kwargs, use_args
from webargs import fields



def hello_teacher(request):
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
        "email": fields.Str(
            required=False,
            missing=None,
        ),
        "birthdate": fields.Str(
            required=False,
            missing=None,
        ),
    },
    location="query",
)
def get_teachers(request, first_name, last_name, email, birthdate):

    students = Teacher.objects.all()
    if first_name:
        students = students.filter(first_name=first_name)
    if last_name:
        students = students.filter(last_name=last_name)
    if email:
        students = students.filter(email=email)
    if birthdate:
        students = students.filter(birthdate=birthdate)
    result = format_records(students)
    return HttpResponse(result)