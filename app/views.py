from urllib import request
from django.views.generic import ListView
from django.http import HttpResponse
from django.shortcuts import redirect, render
from app.forms import StudentForm

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

def Add_Student(request):
    if request.method == "POST":
        firstName = request.POST.get("firstName")
        lastName = request.POST.get("lastName")
        email = request.POST.get("email")
        Student.objects.create(
            first_name = firstName,
            last_name = lastName,
            email = email
        )
        return redirect('student_display')
    return render(request,'app/add_student.html')

def add_Student_Form(request):
    form = StudentForm()
    if request.method == "POST" :
        form = StudentForm(request.POST)
        if form.is_valid():
            Student.objects.create(
                first_name = form.cleaned_data['first_name'],
                last_name = form.cleaned_data['last_name'],
                email = form.cleaned_data['first_name']
            )
            return redirect('student_display')
    return render(
    request,
    'app/add_student_form.html',
    {'form': form}
)