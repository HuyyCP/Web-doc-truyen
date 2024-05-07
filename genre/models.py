from typing import Any
from django.db import models
from django.utils.text import slugify

class Genre(models.Model): 
    genreName = models.CharField(max_length=50, unique=True, null=False, blank=False)
    slug      = models.SlugField(max_length=60, default='')

    def save(self):
        self.slug = slugify(self.title)
        super().save()
