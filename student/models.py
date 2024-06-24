from django.db import models

# Create your models here.@
class Student(models.Model):
    firstname= models.CharField(max_length=20)
    lastname= models.CharField(max_length=20)
    email= models.EmailField()
    date_of_birth= models.DateField()
    code=models.PositiveSmallIntegerField()
    country=models.CharField(max_length=28)
    teacher = models.ForeignKey()
    
    
    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    

