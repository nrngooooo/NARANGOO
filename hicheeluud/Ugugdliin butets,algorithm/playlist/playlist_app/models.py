from django.db import models

# Create your models here.

class Song(models.Model):
    name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    class Meta:
        db_table="song"
class Playlist(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    songs = models.ManyToManyField(Song)
    class Meta:
        db_table="playlist"
    def __str__(self):
        return self.name