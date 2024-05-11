from django.db import models
from django.utils import timezone
from manga.models import Manga

class Chapter(models.Model):
    title       = models.CharField(max_length=100, null=False, blank=False)
    index       = models.IntegerField()
    manga       = models.ForeignKey(Manga, on_delete=models.CASCADE)
    idDrive     = models.CharField(max_length=100, unique=True, null=False, blank=False)
    uploadTime  = models.DateTimeField(auto_now_add=True)

