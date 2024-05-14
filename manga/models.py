from django.db import models
from genre.models import Genre
from author.models import Author
from django.contrib.auth.models import User

class Manga(models.Model):
    title       = models.CharField(max_length=100, null=False, blank=False)
    slug        = models.SlugField(max_length=100, default='')
    description = models.TextField(max_length=200, default='')
    avatarLink  = models.CharField(max_length=200, default='')
    idDrive     = models.CharField(max_length=100, unique=True, null=False, blank=False, default='')
    uploader    = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    author      = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    genres      = models.ManyToManyField(Genre)


 