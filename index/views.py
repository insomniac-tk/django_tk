from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<title>INDEX</title><h1 style=\"text-align : center;font-family: monospace;\"><u>Welcome to the polls app!</u></h1>")