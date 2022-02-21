from django.urls import URLPattern, path
from .views import detail_Student, homePage, list_students

urlpatterns = [
    path('', homePage, name='home'),
    path('list/', list_students, name='student_display'),
    path('detail/<int:student_id>', detail_Student, name='student_detail'),
    
]