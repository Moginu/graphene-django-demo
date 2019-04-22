from django.db import models


class Artist(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    monthly_listeners = models.IntegerField()
    followers = models.IntegerField()
    name = '{} {}'.format(first_name, last_name)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Album(models.Model):
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {} {}'.format(self.name, self.artist.first_name, self.artist.last_name)
