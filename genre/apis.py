from .models import Genre
class GenreAPI:
    def getAllGenres(self):
        return Genre.objects.all()
    
genreAPI = GenreAPI()