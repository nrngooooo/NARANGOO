from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=350)
    author = models.CharField(max_length=350)
    genre = models.CharField(max_length=350)
    year = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    class Meta:
        db_table="book"
