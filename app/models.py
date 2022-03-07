from django.urls import reverse
from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.core.exceptions import ValidationError
# Create validator
def email_validator(email):
    if not str(email).endswith('@esprit.tn'):
        raise ValidationError('Email must end with @esprit.tn')
    return email

# Create your models here.


class User(models.Model):
    first_name = models.CharField(verbose_name="Prénom", max_length=30)
    last_name = models.CharField(verbose_name="Nom", max_length=30)
    email = models.EmailField(verbose_name="Email", null=False,validators=[email_validator])
    def __str__(self):
        return self.first_name + " " + self.last_name
    def get_absolute_url(self):
        return reverse("student_display")
    
    
    

class Student(User):
    # def get_absolute_url(self):
    #     return reverse("student_display")
    pass


class Coach(User):
    pass


class Project(models.Model):
    project_name = models.CharField(
        verbose_name="Titre du projet", max_length=50)
    project_duration = models.IntegerField(
        verbose_name="Durée Estimée", default=0)
    time_allocated = models.IntegerField(verbose_name="Temps Alloué",validators=[MinValueValidator(1,"has to be greater than 0"),MaxValueValidator(100)])
    needs = models.TextField(verbose_name="Besoins", max_length=250)
    description = models.TextField(max_length=250)

    isValid = models.BooleanField(default=False)
    
    creator = models.OneToOneField(
        to = Student, 
        on_delete = models.CASCADE, 
        related_name = "project_owner"
    )
    
    supervisor = models.ForeignKey(
        to=Coach,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="project_coach"
    )
    
    members = models.ManyToManyField(
        to = Student,
        blank = True,
        related_name = 'Les_Membres',
        through = 'MembershipInProject',
    )
    def __str__(self):
        return self.project_name
    
    
class MembershipInProject (models.Model):
    project = models.ForeignKey(
        Project,
        on_delete = models.CASCADE,
    )
    
    student = models.ForeignKey(
        Student,
        on_delete = models.CASCADE,
    )
    
    time_allocated_by_member = models.IntegerField(
        'Temps alloué par le membre',
    )
    
    class Meta:
        unique_together = ("project", "student")