from dataclasses import fields
from django.contrib import admin
from .models import Coach, MembershipInProject, Project,Student

class projectInLine(admin.TabularInline):
    model = Project
    fieldsets = [(None,{'fields':['project_name']})]
    extra = 0

@admin.register(Student)
class studentAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email')
    fields = (('first_name','last_name'),'email')
    inlines = [projectInLine]

@admin.register(Coach)
class coachAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email')
    fields = (('first_name','last_name'),'email')
    inlines = [projectInLine] # bsh njib les information mta3 el table lokhra . 

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name','project_duration','time_allocated','description')
    fieldsets = [
        ('state', {'fields':['isValid']}),
        ('about', {'fields':['project_name','supervisor','needs','description']}),
        ('Time', {'fields':['project_duration','time_allocated']})
    ]
    
# Register your models here.

admin.site.register(Project,ProjectAdmin)
admin.site.register(MembershipInProject)