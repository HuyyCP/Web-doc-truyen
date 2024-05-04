from django.db import models
from manga.models import Manga

class Chapter(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    index = models.IntegerField()
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE)

