from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from webargs.djangoparser import use_kwargs, use_args, parser
from webargs import fields
from teachers.forms import TeacherBaseForm
from courses.models import Course
from teachers.models import Teacher


@parser.use_args(
    {
        "first_name": fields.Str(
            required=False,
        ),
        "text": fields.Str(required=False),
    },
    location="query",
)
def get_teachers(request, params):

    course = Course.objects.all()
    if request.GET.get('featured'):
        selected_course = Course.objects.get(name=request.GET.get('featured')).id
        teachers = Teacher.objects.filter(course=selected_course)
    else:
        teachers = Teacher.objects.all().order_by("id")
        selected_course = ''
    return render(
            request=request,
            template_name="teachers_table.html",
            context={
                "teachers": teachers,
                "courses": course,
                "selected_course": selected_course
            }
        )


@csrf_exempt
def create_teacher(request):
    if request.method == "POST":
        form = TeacherBaseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("teachers:teachers"))

    elif request.method == "GET":
        form = TeacherBaseForm()

    return render(
        request=request,
        template_name="teacher_create.html",
        context={
            "form": form
        }
    )


