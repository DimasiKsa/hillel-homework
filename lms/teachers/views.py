from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def hello_teacher(request):
    return HttpResponse('SUCCESS')