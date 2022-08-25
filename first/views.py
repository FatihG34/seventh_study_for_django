import http
from http.client import HTTPResponse
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request, 'first/index2.html')


def student_page(request):
    return render(request, 'first/student.html')
