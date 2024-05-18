from .models import Genre
class GenreAPI:
    def getAllGenres(self):
        return Genre.objects.all()
    
    def getGenreById(self, genre_id):
        return Genre.objects.get(id=genre_id)
    
    def getGenreBySlug(self, slug):
        return Genre.objects.get(slug=slug)
    
genreAPI = GenreAPI()