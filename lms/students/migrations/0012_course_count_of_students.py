# Generated by Django 3.2.9 on 2021-11-07 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0011_student_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='count_of_students',
            field=models.IntegerField(default=0),
        ),
    ]
