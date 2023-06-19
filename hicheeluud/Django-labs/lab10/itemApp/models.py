from django.db import models
from categoryApp.models import Category
# Create your models here.

class Item(models.Model):
    bname = models.CharField(max_length=256)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    class Meta:
        db_table="baraa"
    def __str__(self):
        return f"{self.bname} ({self.category})"