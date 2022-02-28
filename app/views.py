from django.urls import reverse
from django.views.generic import ListView
from django.http import HttpResponse
from django.shortcuts import redirect, render
from app.forms import StudentForm, StudentModelForm
from django.views.generic.edit import CreateView

from app.models import Project, Student
# Create your views here.

def homePage(request):
    return HttpResponse("<h1>Hello, world. You're at the home page.</h1>")

def list_students(request):
    list = Student.objects.all()
    return render(request, 'app/list_students.html', {'list_students': list})

def detail_Student(request,student_id):
    student = Student.objects.get(id=student_id) #get_objects_or_404(Student, id=student_id)
    return render(request, 'app/detail_Student.html', {'student': student})

def list_projects(request): #function based view
    list = Project.objects.all()
    return render(request, 'app/list_projects.html', {'object_list': list})

class ProjectListView(ListView): #class based view
    model = Project
    template_name = 'app/list_projects.html'
    context_object_name = 'list_projects'

class StudentCreateView(CreateView):
    template_name = 'app/add_student_form.html'
    model = Student
    form_class = StudentModelForm
    def get_success_url(self):
        return reverse("student_display")