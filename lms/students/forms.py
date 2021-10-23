from django.forms import ModelForm, DateInput
from django.core.exceptions import ValidationError
from students.models import Student
import datetime


class StudentCreateForm(ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'birthdate']
        birthdate = {'birthdate': DateInput()}

    def clean_birthdate(self):
        birthdate = self.cleaned_data["birthdate"]
        user_age = (datetime.date.today()-birthdate)
        if user_age.days//365 < 18:
            raise ValidationError(f"the user must only users who are 18 or older")
        return birthdate

    def clean_email(self):
        no_valid_email = ["@xyz.com", "@xzy.com", "@zyx.com"]
        email = self.cleaned_data["email"]
        val_answer = [i for i in no_valid_email if i in email]
        if val_answer != []:
            raise ValidationError(f"Email {val_answer[0]} banned")
        return email

    def clean(self):
        cleaned_data = super().clean()

        first_name = cleaned_data['first_name']
        last_name = cleaned_data['last_name']
        if first_name == last_name:
            raise ValidationError('First and last names can\'t be equal')

        return cleaned_data


class StudentGetForm(ModelForm):
    class Meta:
        pass
