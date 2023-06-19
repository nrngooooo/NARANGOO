from django.db import models

# Create your models here.
class Club(models.Model):
    cname = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.cname
class Comedian(models.Model):
    coname = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    image = models.ImageField(blank=True, null=True, upload_to='static/images')
    club = models.ForeignKey(Club, related_name='clubs', on_delete=models.CASCADE)
    def __str__(self):
        return self.coname