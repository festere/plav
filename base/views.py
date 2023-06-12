from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from colorama import Fore


# Create your views here.
def home(request):
    return render(request, 'home.html')


# Errors handling
def handler404(request, exception):
    return render(request, '404.html', status=404)

def handler409(request, exception):
    return render(request, '409.html', status=409)

def handler500(request, exception):
    return render(request, '500.html', status=404)
