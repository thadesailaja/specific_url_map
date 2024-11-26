from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def nalgame(request):
    return HttpResponse('<h1><i>Cricket is the national game of Australia!!</i></h1>')
