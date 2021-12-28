from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
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


class CreateTeacher(LoginRequiredMixin, CreateView):
    # form_class = StudentCreateForm
    template_name = "teacher_create.html"
    fields = "__all__"
    model = Teacher
    initial = {
        "first_name": "default",
        "last_name": "default",
    }
    success_url = reverse_lazy("teachers:list")

