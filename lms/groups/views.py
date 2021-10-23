from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from webargs.djangoparser import use_kwargs, use_args, parser
from webargs import fields
from groups.utils import format_records
from groups.models import Group
from groups.forms import GroupCreateForm


def hello_groups(request):
    return HttpResponse('SUCCESS')


@use_args(
    {
        "first_name": fields.Str(
            required=False,

        ),
        "last_name": fields.Str(
            required=False,

        ),
        "num_group": fields.Str(
            required=False,

        ),
        "text": fields.Str(
            required=False,

        ),
    },
    location="query",
)
def get_groups(request, params):
    teachers = Group.objects.all().order_by('-id')
    for param_name, param_val in params.items():
        teachers = teachers.filter(**{param_name: param_val})
    result = format_records(teachers)
    return HttpResponse(result)


@csrf_exempt
def create_groups(request):

    if request.method == 'POST':
        form = GroupCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/get_groups')

    elif request.method == 'GET':
        form = GroupCreateForm()

    form_html = f"""
    <form method="POST">
      {form.as_p()}
      <input type="submit" value="Create">
    </form>
    """

    return HttpResponse(form_html)