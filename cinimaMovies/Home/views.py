from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
# Home view page 
def HomePageView(request):

    movieList = Movies.objects.all().order_by('-releaseDate')

    tamplate = 'index.html'
    context = {
         'movies' : movieList,

    }
    return render(request,tamplate,context)





def MoviesDetail(request , movieTitle):
     movies = Movies.objects.filter(movieTitle=movieTitle)     
     
     for movie in movies:
          Director = movie.Director.all().values('Director')
          Actors = movie.Actors.all().values('Actor')
          types =  movie.typeMovie.all().values('Type')
          idMovie =  movie.id  

     Reviews = MoviesReview.objects.filter(MoviesTilte=idMovie)
     
     context = {
          'movieList' : movies,
          'Director' : Director,
          'Actors' : Actors,
          'Reviews' : Reviews,  
          'types' : types,
     }


     return render(request,'Movies/MovieDetail.html',context)


def reviewDetail(request,movieTitle,reviewname):

     movies = Movies.objects.filter(movieTitle=movieTitle)     
     
     for movie in movies:
          Director = movie.Director.all().values('Director')
          Actors = movie.Actors.all().values('Actor')
          types =  movie.typeMovie.all().values('Type')
          idMovie =  movie.id  

     Reviews = MoviesReview.objects.filter(MoviesTilte=idMovie)
     Types = TypeMovies.objects.all()
     context = {
          'movieList' : movies,
          'Director' : Director,
          'Actors' : Actors,
          'Reviews' : Reviews,  
          'types' : types,
          'Types':Types,
     }

     return render(request,'Movies/reviewDetail.html',context)
    



