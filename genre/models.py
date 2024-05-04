from django.db import models

class Genre(models.Model): 
    genreName = models.CharField(max_length=50, null=False, blank=False)
