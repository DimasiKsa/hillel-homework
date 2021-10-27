from django import forms
from django.forms import ModelForm, DateInput
from django.core.exceptions import ValidationError
from students.models import Student
import datetime


class StudentCreateForm(ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'birthdate', 'password1', 'password2']
        birthdate = {'birthdate': DateInput()}
        widgets = {
            'password1': forms.PasswordInput(),
            'password2': forms.PasswordInput(),
        }

    def clean_birthdate(self):
        birthdate = self.cleaned_data["birthdate"]
        user_age = (datetime.date.today()-birthdate)
        how_old_student = user_age.days//365
        if how_old_student < 18:
            raise ValidationError(f"the user must only users who are 18 or older")
        return birthdate

    def clean_email(self):
        no_valid_email = ["@xyz.com", "@xzy.com", "@zyx.com"]
        email = self.cleaned_data["email"]
        val_answer = [i for i in no_valid_email if i in email]
        if not val_answer[0]:
            raise ValidationError(f"Email {val_answer[0]} banned")
        email = self.cleaned_data['email'].strip()
        if Student.objects.filter(email__iexact=email).exists():
            raise ValidationError(f'Student with this Email({email}) already exists')
        return email

    def clean(self):
        cleaned_data = super().clean()

        first_name = cleaned_data['first_name']
        last_name = cleaned_data['last_name']
        password1 = cleaned_data['password1']
        password2 = cleaned_data['password2']
        if password1 != password2:
            raise ValidationError('Can you please confirm your password for security purposes?')
        if first_name == last_name:
            raise ValidationError('First and last names can\'t be equal')

        return cleaned_data

    @staticmethod
    def normalize_name(name):
        return name.lower().strip().capitalize()

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']

        return self.normalize_name(first_name)

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']

        return self.normalize_name(last_name)



class StudentGetForm(ModelForm):
    class Meta:
        pass
