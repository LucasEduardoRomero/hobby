from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("<h2 style='text-shadow:2px 2px 2px yellow'>Hello, world. You're at the app index.</h2>")