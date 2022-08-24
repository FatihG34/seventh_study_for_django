import http
from http.client import HTTPResponse
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return HttpResponse('hi')


def student_num(request):
    num_of_stdnt = 22
    return HttpResponse(f'Hi, in this school, we have {num_of_stdnt} students')
