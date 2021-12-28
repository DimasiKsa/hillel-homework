from django.utils.html import format_html
from django.contrib import admin
from django import forms
from .models import Student, UserProfile, CustomUser


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'age', 'birthdate']
    search_fields = ['first_name__startswith', 'last_name__icontains', 'email']
    list_filter = ['first_name']
    ordering = ['first_name']


admin.site.register(UserProfile)
admin.site.register(CustomUser)