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
from students.views import create_student, hello_students, get_students, update_student
from django.urls import path

app_name = 'students'

urlpatterns = [
    path('', hello_students, name='hello'),
    path('students/', get_students, name='list'),
    path('create/', create_student, name='create'),
    path('update/<int:pk>/', update_student, name='update'),
]
