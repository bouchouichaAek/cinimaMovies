from django.db import models


# MoviesDatabases

import datetime
YEAR_CHOICES = [(r,r) for r in range(1924, datetime.date.today().year+1)]


class Director(models.Model):#director of the Movies table relation many to many with Movies table
    Director = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.Director

class ActorsTable(models.Model): # Actors of the Movies table relation many to many with Movies table
    Actor = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.Actor



class TypeMovies(models.Model): #type Movies table relation many to many with Movies table
    Type = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.Type


class Movies(models.Model): # Movies table
    movieTitle = models.CharField(max_length=100,unique=True)
    description = models.CharField(max_length=255,unique=True)
    imageMovie = models.ImageField(null = True,blank = True,unique=True)
    releaseDate = models.IntegerField(('years'),choices=YEAR_CHOICES,null = True,blank = True)
    duration = models.CharField(max_length = 10 ,null = True,blank = True)
    typeMovie = models.ManyToManyField(TypeMovies)
    Director = models.ManyToManyField(Director)
    Actors = models.ManyToManyField(ActorsTable)
    

    def __str__(self):
        return self.movieTitle


class MoviesReview(models.Model):
    MoviesTilte = models.ForeignKey(Movies,on_delete=models.CASCADE)
    ReviewAuthor = models.ForeignKey('auth.User',on_delete=models.CASCADE,blank=False,null=False)
    reviewTilte = models.CharField(max_length = 100 ,null = True,blank = True)
    Moviesreview = models.TextField()
    Timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)

    def __str__(self):
        return self.MoviesTilte