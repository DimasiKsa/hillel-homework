from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, CreateView
from webargs.djangoparser import use_kwargs, use_args, parser
from webargs import fields
from teachers.forms import TeacherBaseForm
from courses.models import Course
from teachers.models import Teacher


class GetTeacher(TemplateView):
    model = Teacher
    template_name = "teachers_table.html"
    success_url = reverse_lazy("students:list")

    def get(self, request, *args, **kwargs):
        course = Course.objects.all()
        if request.GET.get('featured'):
            selected_course = Course.objects.get(name=request.GET.get('featured')).id
            teachers = Teacher.objects.filter(course=selected_course)
            context = {
                "teachers": teachers,
                "courses": course,
                "selected_course": selected_course
            }
        else:
            teachers = Teacher.objects.all().order_by("id")
            context = {
                "teachers": teachers,
                "courses": course
            }

        return render(request, 'teachers_table.html', context)


class CreateTeacher(CreateView):
    # form_class = StudentCreateForm
    template_name = "teacher_create.html"
    fields = "__all__"
    model = Teacher
    initial = {
        "first_name": "default",
        "last_name": "default",
    }
    success_url = reverse_lazy("teachers:list")

