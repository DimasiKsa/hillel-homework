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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import handler404
import debug_toolbar
from django.urls import include, path
from students.views import IndexPage, RegistrationStudent


handler404 = 'students.views.page_error.view_404'

urlpatterns = [
    path("", IndexPage.as_view(), name="hello"),
    path("admin/", admin.site.urls),
    path("__debug__/", include(debug_toolbar.urls)),
    path("students/", include("students.urls")),
    path("teachers/", include("teachers.urls")),
    path("registration/", RegistrationStudent.as_view(), name="registration")
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
