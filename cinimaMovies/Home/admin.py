from django.contrib import admin
from .models import Movies,TypeMovies,Director,ActorsTable,MoviesReview

# Register your models here.

class DetailMovies(admin.ModelAdmin):
    list_display = ["__str__","releaseDate","duration"]

class DetailReview(admin.ModelAdmin):
    list_display = ["__str__","ReviewAuthor"]

admin.site.register(Movies,DetailMovies)
admin.site.register(TypeMovies)
admin.site.register(Director)
admin.site.register(ActorsTable)
admin.site.register(MoviesReview,DetailReview)