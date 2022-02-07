from django.db import models

# Create your models here.
class Client(models.Model):
    first_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    number = models.IntegerField(default=0)

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(verbose_name="Email", null= False) #verbose_name is for setting a default name for the attribute

class Student(User): #heritage de User
    pass #no need to define anything

class Supervisor(User):
    pass #no need to define anything, just inherit from User

class Project(models.Model):
    name = models.CharField(max_length=50)
    duration = models.IntegerField(default=0)
    needs = models.TextField(max_length=250)
    time_allocated = models.IntegerField(default=0)
    description = models.TextField(max_length=250)
    isValid = models.BooleanField(default=False)
    supervisor = models.ForeignKey(Supervisor, on_delete=models.SET_NULL,blank=True,null=True,
                                   related_name='Project_sup')
    creator = models.OneToOneField(Student, on_delete=models.CASCADE,blank=True,null=True)
    #many To Many between Student and Project
    participants = models.ManyToManyField(Student, blank=True, related_name='Project_students')#,through="student_project") #through = is what is t"table intérmediaire"

class MembershipProject(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE,blank=True,null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE,blank=True,null=True)
    time_allocated_by_member = models.IntegerField(default=0)