from django.contrib import admin
from .models import Course, UserType


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'count_of_students']
    ordering = ['count_of_students']


admin.site.register(UserType)

