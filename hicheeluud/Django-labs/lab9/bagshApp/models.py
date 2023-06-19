from django.db import models
from tenhimApp.models import Tenhim

# Create your models here.
class Bagsh(models.Model):
    bovog = models.CharField(max_length=256)
    bname = models.CharField(max_length=256)
    tenhim = models.ForeignKey(Tenhim,on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=32)
    password_confirm = models.CharField(max_length=32)
    class Meta:
        db_table="bagsh"
    def __str__(self):
        return f"{self.bovog[0]}. {self.bname}"