from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.
class Actors(models.Model):
    name = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to='actors', blank=True)

    def __str__(self):
        return '{}'.format(self.name)
class Language(models.Model):
    name=models.CharField(max_length=200, unique=True)

    def __str__(self):
        return '{}'.format(self.name)
class Genre(models.Model):
    name=models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=250,)
    def __str__(self):
        return '{}'.format(self.name)
    def get_url(self):
        return reverse('GenreMovies',args=[self.id])

class Movies(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    plot = models.TextField(blank=True)
    budget = models.IntegerField()
    director = models.CharField(max_length=200)
    time= models.IntegerField()
    release_date= models.DateField()
    language=models.ManyToManyField(Language)
    actors=models.ManyToManyField(Actors)
    genres=models.ManyToManyField(Genre)
    trailer=models.URLField(max_length = 200)
    image = models.ImageField(upload_to='movie',blank=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE,default=1)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


    def get_url(self):
        return  reverse('movie:MovieDetails',args=[self.slug])
    def __str__(self):
        return '{}'.format(self.name)

    # def get_url(self):
    #     return reverse('movie:MovieList', args=[self.slug])
class Review(models.Model):
    count = models.Aggregate(primary_key=True,default =0)
    rating = models.IntegerField()
    review=models.TextField(blank=True)
    movie=models.ForeignKey(Movies,on_delete=models.CASCADE)
    class meta:
        db_table='Review'
    def avg_rating(self):
        return self.rating // self.count

    # def __str__(self):
    #     return '{}'.format(self.name)
