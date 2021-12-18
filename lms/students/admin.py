from django.contrib import admin
from .models import Student, UserProfile, CustomUser


admin.site.register(Student)
admin.site.register(UserProfile)
admin.site.register(CustomUser)

# Register your models here.
