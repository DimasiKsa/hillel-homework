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
from students.views.students_views import (CreateStudent, IndexPage, GetStudent, UpdateStudent,
                            DeleteStudent, LoginStudent, LogoutStudent, ActivateUser, RegistrationStudent)
from django.urls import path


app_name = "students"

urlpatterns = [
    path("hello/", IndexPage.as_view(), name="hello"),
    path("list/", GetStudent.as_view(), name="list"),
    path("create/", CreateStudent.as_view(), name="create"),
    path("update/<int:pk>/", UpdateStudent.as_view(), name="update"),
    path("delete/<int:pk>/", DeleteStudent.as_view(), name="delete"),
    path("login", LoginStudent.as_view(), name="login"),
    path("logout", LogoutStudent.as_view(), name="logout"),
    path("logout", LogoutStudent.as_view(), name="logout"),
    path("registration/", RegistrationStudent.as_view(), name="registration"),
    path('activate/<str:uidb64>/<str:token>', ActivateUser.as_view(),
         name='activate')
]
