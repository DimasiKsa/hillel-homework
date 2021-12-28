from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import EmailMessage
from django.forms.utils import ErrorList
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode
from django.views.generic import CreateView, TemplateView, UpdateView, DeleteView, RedirectView
from students.models import Student
from courses.models import Course
from students.forms import RegistrationStudentForm
from students.services.emails import send_registration_email
from students.token_generator import TokenGenerator


class IndexPage(TemplateView):
    template_name = "index.html"


class GetStudent(TemplateView):
    model = Student
    template_name = "students_table.html"
    success_url = reverse_lazy("students:list")

    def get(self, request, *args, **kwargs):
        course = Course.objects.all()
        if request.GET.get('featured'):
            selected_course = Course.objects.get(name=request.GET.get('featured')).id
            students = Student.objects.filter(course=selected_course)
            context = {
                "students": students,
                "courses": course,
                "selected_course": selected_course
            }
        else:
            students = Student.objects.all().order_by("id")
            context = {
                "students": students,
                "courses": course
            }

        return render(request, 'students_table.html', context)


class CreateStudent(LoginRequiredMixin, CreateView):
        template_name = "students_create.html"
        fields = "__all__"
        model = Student
        initial = {
            "first_name": "default",
            "last_name": "default",
        }
        success_url = reverse_lazy("students:list")

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


class UpdateStudent(LoginRequiredMixin, UpdateView):
    model = Student
    template_name = "students_update.html"
    fields = "__all__"
    success_url = reverse_lazy("students:list")


class DeleteStudent(LoginRequiredMixin, DeleteView):
    model = Student
    template_name = "student_delete.html"
    success_url = reverse_lazy("students:list")


class LoginStudent(LoginView):
    pass


class LogoutStudent(LogoutView):
    template_name = "index.html"


class RegistrationStudent(CreateView):
    form_class = RegistrationStudentForm
    template_name = "registration/registration.html"
    success_url = reverse_lazy("students:hello")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.is_active = False
        self.object.save()
        send_registration_email(request=self.request,
                                user_instance=self.object)
        return super().form_valid(form)


class ActivateUser(RedirectView):
    url = reverse_lazy('students:list')

    def get(self, request, uidb64, token, *args, **kwargs):
        print(f"uidb64: {uidb64}")
        print(f"token: {token}")

        try:
            user_pk = force_bytes(urlsafe_base64_decode(uidb64))
            print(f"user_pk: {user_pk}")
            current_user = User.objects.get(pk=user_pk)
        except (User.DoesNotExist, ValueError, TypeError):
            return HttpResponse("Wrong data")

        if current_user and TokenGenerator().check_token(current_user, token):
            current_user.is_active = True
            current_user.save()

            login(request, current_user)
            return super().get(request, *args, **kwargs)
        return HttpResponse("Wrong data")

