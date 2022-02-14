from django.http import HttpResponse
from django.shortcuts import render

from app.models import Student

# Create your views here.

def homePage(request):
    return HttpResponse("<h1>Hello, world. You're at the home page.</h1>")

def list_students(request):
    list = Student.objects.all()
    return render(request, 'app/list_students.html', {'list_students': list})