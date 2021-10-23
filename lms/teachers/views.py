from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from teachers.models import Teacher
from teachers.utils import format_records
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from webargs.djangoparser import use_kwargs, use_args
from webargs import fields
from teachers.forms import TeacherCreateForm
from webargs.djangoparser import use_kwargs, use_args, parser
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

    teachers = Teacher.objects.all().order_by('-id')
    for param_name, param_val in params.items():
        teachers = teachers.filter(**{param_name: param_val})
    result = format_records(teachers)
    return HttpResponse(result)


@csrf_exempt
def create_teacher(request):

    if request.method == 'POST':
        form = TeacherCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/get_teachers')

    elif request.method == 'GET':
        form = TeacherCreateForm()

    form_html = f"""
    <form method="POST">

      {form.as_p()}
      <input type="submit" value="Create">
    </form>
    """

    return HttpResponse(form_html)
