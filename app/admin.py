from dataclasses import fields
from django.contrib import admin,messages
from .models import Coach, MembershipInProject, Project,Student

# filters 

class ProjectDurationFilter(admin.SimpleListFilter):
    title = 'Duration' #will be displayed in the filter list
    parameter_name = 'project_duration' #the attribute name of the field in the model we want to filter WITH
    
    def lookups(self, request, model_admin):
        return (
            ('1 month', ('less than 1 month')),
            ('3 months', ('less than 3 months')),
        )
    def queryset(self, request, queryset):
        if self.value() == '1 month':
            return queryset.filter(project_duration__lte=30)
        if self.value() == '3 months':
            return queryset.filter(project_duration__gte=90)

class projectInLine(admin.StackedInline): #we can use StackedInline or TabularInline // difference in the displayment
    model = Project
    # fieldsets = [(None,{'fields':['project_name']})]
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
    search_fields = ['first_name','last_name'] # selon hetha bsh ya3ml el recherche fl autocomplete mbaad

def set_Valid(modeladmin, request, queryset):
    rows_updated = queryset.update(isValid=True)
    if rows_updated == 1:
        message = "1 project was "
    else:
        message = f"{rows_updated} projects were "
    messages.success(request, message="%s successfully marked as valid" % message)
    
set_Valid.short_description = "Mark selected projects as valid"


class ProjectAdmin(admin.ModelAdmin):
    def set_InValid(modeladmin, request, queryset):
        rows_updated = queryset.filter(isValid=False)
        if rows_updated.count() > 0:  
            messages.error(request, f"{rows_updated.count()} already marked as invalid" )
        else: # if rows selected are not ALREADY marked as invalid
            if rows_updated == 1:
                message = "1 project was "
            else:
                message = f"{rows_updated} projects were "
            messages.success(request, message="%s successfully marked as Invalid" % message) 
    set_InValid.short_description = "Mark selected projects as Invalid"

    actions = [set_Valid,'set_InValid']
    actions_on_bottom = True
    actions_on_top = True
    list_display = ('project_name','project_duration','time_allocated','description')
    fieldsets = [
        ('state', {'fields':['isValid']}),
        ('about', {'fields':['project_name','supervisor','needs','description', 'creator']}),
        ('Time', {'fields':['project_duration','time_allocated']})
    ]
    # radio_fields = { "supervisor": admin.VERTICAL }
    autocomplete_fields = ['supervisor']
    list_filter = (
        'supervisor',
        'isValid',
        ProjectDurationFilter, 
    )
    
# Register your models here.

admin.site.register(Project,ProjectAdmin)
admin.site.register(MembershipInProject)

