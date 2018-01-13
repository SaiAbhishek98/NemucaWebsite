from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<p>This is the android event pannel just temporary wont be using it anymore</p>")
