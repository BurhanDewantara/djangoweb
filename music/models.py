from django.db import models
from django.urls import reverse

# Create your models here.
class Album(models.Model):
    artist = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    genre = models.CharField(max_length=100)
    logo = models.CharField(max_length=500)

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.pk})

    def __str__ (self):
        return self.artist + ' - ' + self.title


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    file_ext = models.CharField(max_length=10)
    is_favorite = models.BooleanField(default=False)

    def __str__ (self):
        return self.album.title + ' - ' + self.title

    
