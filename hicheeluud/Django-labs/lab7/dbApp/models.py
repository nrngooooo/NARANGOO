from django.db import models
# Create your models here.
class Branch(models.Model):
    bname = models.CharField(max_length=256)
    class Meta:
        db_table="tbl_branch"
    def __str__(self):
        return self.bname