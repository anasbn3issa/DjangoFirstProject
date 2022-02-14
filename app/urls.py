from django.urls import URLPattern, path
from .views import homePage, list_students

urlpatterns = [
    path('', homePage, name='home'),
    path('list/', list_students, name='student_display'),
    
]