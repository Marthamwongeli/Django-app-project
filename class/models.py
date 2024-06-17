from django.db import models
class Class(models.Model):
    class_id= models.PositiveSmallIntegerField()
    name= models.CharField(max_length=20)
    teacher= models.CharField(max_length=20)
    room_number= models.PositiveSmallIntegerField()
    class_size=models.IntegerField()
    start_time=models.CharField(max_length=28)
    end_time=models.CharField(max_length=20)
    school_year= models.IntegerField()
    description=models.TextField(max_length=50)
    created_at=models.CharField(max_length=20)
    
    
    
    
    def __str__(self):
        return f"{self.name} {self.class_id}"
# Create your models here.
