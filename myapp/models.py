from django.db import models
class Student(models.Model):
    name=models.CharField(max_length=64)
    rollno=models.IntegerField()
    marks=models.IntegerField()
    gf=models.CharField(max_length=64)
    bf=models.CharField(max_length=64)
    
