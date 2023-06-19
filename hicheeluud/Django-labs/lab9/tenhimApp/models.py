from django.db import models

# Create your models here.

class Tenhim(models.Model):
    tname = models.CharField(max_length=256)
    class Meta:
        db_table="tenhim"
    def __str__(self):
        return self.tname