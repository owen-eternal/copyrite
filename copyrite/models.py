from django.db import models


class Artist(models.Model):
    artist_name = models.CharField(max_length=50)
    record_label = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.artist_name


class Album(models.Model):
    album_name = models.CharField(max_length=50)
    release_date = models.DateField()
    date = models.DateTimeField(auto_now_add=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.album_name


class Track(models.Model):
    title = models.CharField(max_length=50)
    duration = models.IntegerField()
    genre = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
