from django.db import models


# Create your models here.
# Define blueprints for database here.

# Each album has a unique primary key
class Album(models.Model):
    # Each variable represents a column in the database
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)

    # String representation of object
    def __str__(self):
        return self.album_title + ' - ' + self.artist

class Song(models.Model):
    # Cascade means delete all other songs linked to album
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title