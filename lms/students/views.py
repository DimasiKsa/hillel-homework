from django.core.exceptions import BadRequest
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from students.models import Student, Course, Teacher
from students.utils import format_records
from webargs.djangoparser import use_kwargs, use_args, parser
from webargs import fields
from students.forms import StudentCreateForm, StudentUpdateForm, TeacherBaseForm


def hello_students(request):
    return render(
        request=request,
        template_name="index.html",
        context={
            "param": "some text"
        }
    )


@parser.error_handler
def handle_error(error, req, schema, *, error_status_code, error_headers):
    raise BadRequest(error.messages)


@parser.use_args(
    {
        "first_name": fields.Str(
            required=False,
        ),
        "text": fields.Str(required=False),
    },
    location="query",
)
def get_students(request, params):

    course = Course.objects.all()
    if request.GET.get('featured'):
        selected_course = Course.objects.get(name=request.GET.get('featured')).id
        students = Student.objects.filter(course=selected_course)
    else:
        students = Student.objects.all().order_by("id")
        selected_course = ''
    return render(
            request=request,
            template_name="students_table.html",
            context={
                "students": students,
                "courses": course,
                "selected_course": selected_course
            }
        )


@csrf_exempt
def create_student(request):
    if request.method == "POST":
        form = StudentCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("students:list"))

    elif request.method == "GET":
        form = StudentCreateForm()

    return render(
        request=request,
        template_name="students_create.html",
        context={
            "form": form
        }
    )


@csrf_exempt
def update_student(request, pk):

    student = get_object_or_404(Student, id=pk)

    if request.method == "POST":
        form = StudentUpdateForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect((reverse("students:list")))

    elif request.method == "GET":
        form = StudentUpdateForm(instance=student)

    return render(
        request=request,
        template_name="students_update.html",
        context={
            "form": form
        }
    )


def delete_student(request, pk):
    student = get_object_or_404(Student, id=pk)
    student.delete()

    return HttpResponseRedirect(reverse("students:list"))


def view_404(request, exception):
    return render(request, "404.html")


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
            return HttpResponseRedirect(reverse("students:teachers"))

    elif request.method == "GET":
        form = TeacherBaseForm()

    return render(
        request=request,
        template_name="teacher_create.html",
        context={
            "form": form
        }
    )


