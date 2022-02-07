from django.contrib import admin
from .models import Client,Project,Supervisor,Student

# Register your models here.

admin.site.register(Client)
admin.site.register(Project)
admin.site.register(Supervisor)
admin.site.register(Student)