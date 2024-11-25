from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request, 'main/index.html')
def new(request):
    return HttpResponse("<h1>Это вторая страница моего проекта на django</h1>")