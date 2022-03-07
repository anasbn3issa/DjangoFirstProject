from django.urls import URLPattern, path
from .views import StudentCreateView, StudentDeleteBox, deleteBox, detail_Student, homePage, list_projects, list_students,ProjectListView,StudentUpdateView
urlpatterns = [
    path('', homePage, name='home'),
    path('list/', list_students, name='student_display'),
    path('projects/', list_projects, name='project_display'),
    path('classprojects/',ProjectListView.as_view(), name="classprojects"),
    path('detail/<int:student_id>', detail_Student, name='student_detail'),
    #path('student/add', Add_Student, name='add_student'),
    
    path('student/add', StudentCreateView.as_view(), name='create_student'),
    path('student/update/<int:pk>', StudentUpdateView.as_view(), name='update_student'),
    path('student/delete/<int:idToBeDeleted>', deleteBox, name='delete_student'),

    
    
]