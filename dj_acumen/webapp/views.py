from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# Loads the first page
def index(request):
    return render(request, 'webapp/index.html')
#Experimentation purposes
def vv(request):
    return render(request, 'webapp/view.html')
