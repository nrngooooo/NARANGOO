from django.db import models
from departmentApp.models import Department
# Create your models here.
class Student(models.Model):
    stlast = models.CharField(max_length=256)
    stname = models.CharField(max_length=256)
    depcode = models.ForeignKey(Department, on_delete=models.CASCADE)
    class Meta:
        db_table="tbl_student"
    def __str__(self):
        return f"{self.stlast[0]}. {self.stname} ({self.depcode})"