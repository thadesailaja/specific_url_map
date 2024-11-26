from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def nalgame(request):
    return HttpResponse('<h1>Sumo is the national game of japan</h1>')
