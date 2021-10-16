# from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.shortcuts import render


def index(request):
    return HttpResponse("Index")

def api():
    return HttpResponse("Index")

def hello(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def hello2(request):
   today = datetime.datetime.now().date()
   return render(request, "hello.html", {"today" : today})