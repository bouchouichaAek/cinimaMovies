from django.urls import path,include
from .views import MoviesDetail,reviewDetail


urlpatterns = [
    path('<str:movieTitle>/',MoviesDetail , name = 'movie'),
    path('<str:movieTitle>/<str:reviewname>/',reviewDetail , name = 'review'),
]