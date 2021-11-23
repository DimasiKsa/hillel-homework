from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import BadRequest
from django.db.models import Q
from django.forms.utils import ErrorList
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, TemplateView, UpdateView, DeleteView
from students.models import Student
from webargs.djangoparser import use_kwargs, use_args, parser
from webargs import fields
from students.forms import StudentCreateForm, StudentUpdateForm
from courses.models import Course


class IndexPage(LoginRequiredMixin, TemplateView):
    template_name = "index.html"


@parser.error_handler
def handle_error(error, req, schema, *, error_status_code, error_headers):
    raise BadRequest(error.messages)


# class GetStudent(TemplateView):
#     model = Student
#     template_name = "students_table.html"
#     success_url = reverse_lazy("students:list")
#
#     def get(self, request, *args, **kwargs):
#         query = request.GET.get('featured')
#         selected_course = Course.objects.get(name=request.GET.get('featured')).id
#             return Student.objects.filter(course=selected_course)
#         else:
#             return Student.objects.all().order_by("id")
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

class CreateStudent(CreateView):
    # form_class = StudentCreateForm
    template_name = "students_create.html"
    fields = "__all__"
    model = Student
    initial = {
        "first_name": "default",
        "last_name": "default",
    }
    success_url = reverse_lazy("students:list")

    #
    # def get_success_url(self):
    #     return reverse("students:list")
    def form_valid(self, form):
        self.object = form.save(commit=False)
        first_name = form.cleaned_data["first_name"]
        last_name = form.cleaned_data["last_name"]
        if first_name == last_name:
            form._errors["first_name"] = ErrorList(["dsadas"])
            form._errors["last_name"] = ErrorList(
                [u"You already have an email with that name man."])
            return super().form_invalid(form)
        return super().form_valid(form)


class UpdateStudent(UpdateView):
    model = Student
    template_name = "students_update.html"
    fields = "__all__"
    success_url = reverse_lazy("students:list")


class DeleteStudent(DeleteView):
    model = Student
    template_name = "students_table.html"
    success_url = reverse_lazy("students:list")



