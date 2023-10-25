from django.shortcuts import render
from django.http import HttpResponse
#from . import Project
# Create your views here.

def receipes(request):
    return render(request, "receipes/receipes.html")
