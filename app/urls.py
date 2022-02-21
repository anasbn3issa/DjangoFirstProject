from django.urls import URLPattern, path
from .views import detail_Student, homePage, list_projects, list_students,ProjectListView

urlpatterns = [
    path('', homePage, name='home'),
    path('list/', list_students, name='student_display'),
    path('projects/', list_projects, name='project_display'),
    path('classprojects/',ProjectListView.as_view(), name="classprojects"),
    path('detail/<int:student_id>', detail_Student, name='student_detail'),
    
]