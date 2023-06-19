from django.db import models

# Create your models here.
class Department(models.Model):
    depname = models.CharField(max_length=256)
    class Meta:
        db_table="tbl_department"
    def __str__(self):
        return self.depname