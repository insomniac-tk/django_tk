from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<title>Welcome to Polls!</title>Hello, world. You're at the polls index.")