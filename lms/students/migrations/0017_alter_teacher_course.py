# Generated by Django 3.2.9 on 2021-11-10 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0016_alter_course_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='course',
            field=models.ManyToManyField(related_name='teachers', to='students.Course'),
        ),
    ]
