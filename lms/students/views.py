from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def hello_students(request):
    return HttpResponse('SUCCESS')