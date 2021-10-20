from django.shortcuts import render
from teachers.models import Teacher
from teachers.utils import format_records
from django.http import HttpResponse
# Create your views here.
from webargs.djangoparser import use_kwargs, use_args
from webargs import fields



def hello_teacher(request):
    return HttpResponse('SUCCESS')

@use_args(
    {
        "first_name": fields.Str(
            required=False,

        ),
        "last_name": fields.Str(
            required=False,

        ),
        "email": fields.Str(
            required=False,

        ),
        "birthdate": fields.Str(
            required=False,

        ),
    },
    location="query",
)
def get_teachers(request, params):

    teachers = Teacher.objects.all()
    for param_name, param_val in params.items():
        teachers = teachers.filter(**{param_name: param_val})
    result = format_records(teachers)
    return HttpResponse(result)