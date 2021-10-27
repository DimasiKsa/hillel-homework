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
from teachers.views import hello_teacher, get_teachers, create_teacher, update_teacher
from django.urls import path

app_name = 'teachers'

urlpatterns = [
    path('', hello_teacher, name='hello'),
    path('teachers/', get_teachers, name='list'),
    path('create_teacher/', create_teacher, name='crate'),
    path('update_teachers/<int:pk>/', update_teacher, name='update'),
]
