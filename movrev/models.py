from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Movie(models.Model):
    movietitle=models.CharField(max_length=255)
    movreleasedate=models.DateField()
    movgenre=models.TextField()

    def __str__(self):
        return self.movietitle

    class Meta:
        db_table='movie'

class Review(models.Model):
    movieid=models.ForeignKey(Movie, on_delete=models.DO_NOTHING)
    reviewdate=models.DateField()
    review=models.TextField()

    def __str__(self):
        return self.review

    class Meta:
        db_table='review'