from django.shortcuts import render


# Import HttpResponse to send text-based responses
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('<h1>Hello I work!<h1>')


def new(request):
    return HttpResponse('<h2> New Page <h2>')