from django.db import models

# Create your models here.
class Course(models.Model):
    course_name=models.CharField(max_length=20)
    description=models.CharField(max_length=20)
    duration=models.CharField(max_length=10)
    fee=models.IntegerField()
    level=models.CharField(max_length=10)

