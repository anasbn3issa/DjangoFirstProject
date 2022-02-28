from django.urls import URLPattern, path
from .views import add_Student_Form, detail_Student, homePage, list_projects, list_students,ProjectListView,Add_Student

urlpatterns = [
    path('', homePage, name='home'),
    path('list/', list_students, name='student_display'),
    path('projects/', list_projects, name='project_display'),
    path('classprojects/',ProjectListView.as_view(), name="classprojects"),
    path('detail/<int:student_id>', detail_Student, name='student_detail'),
    #path('student/add', Add_Student, name='add_student'),
    path('student/add', add_Student_Form, name='add_student'),
    path('student/add2', add_Student_Form, name='add_student_form'),

    
    
]