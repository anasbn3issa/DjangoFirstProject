from django.db import models

# Create your models here.
class Client(models.Model):
    first_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    number = models.IntegerField(default=0)
