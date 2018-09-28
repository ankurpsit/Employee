from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length = 30)
    dob = models.DateField()
    emailid = models.EmailField(max_length = 50)
    contact = models.CharField(max_length = 10)