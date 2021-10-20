"""lms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from students.views import hello_students
from groups.views import hello_groups
from teachers.views import hello_teacher
from students.views import get_students
from teachers.views import get_teachers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', hello_students),
    path('groups/', hello_groups),
    path('teachers/', hello_teacher),
    path('students_get/', get_students),
    path('get_teachers/', get_teachers),

]
