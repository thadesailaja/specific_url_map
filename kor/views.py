from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def nalgame(request):
    return HttpResponse('<h1>Teakwound is the national game of korea</h1>')
