from django.db import models

# Create your models here.

class Category(models.Model):
    cname=models.CharField(max_length=256)

    class Meta:
        db_table = "category"
    def __str__(self):
        return self.cname
    
class Product(models.Model):
    bname = models.CharField(max_length=256)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "product"
    def __str__(self):
        return f"{self.bname} ({self.category})"