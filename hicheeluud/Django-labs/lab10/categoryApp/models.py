from django.db import models
# Create your models here.

class Category(models.Model):
    catname = models.CharField(max_length=256)
    class Meta:
        db_table="turul"
    def __str__(self):
        return self.catname