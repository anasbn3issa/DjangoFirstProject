from django.contrib import admin
from .models import Coach, Project,Student

# Register your models here.

admin.site.register(Project)
admin.site.register(Coach)
admin.site.register(Student)