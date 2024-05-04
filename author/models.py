from django.db import models

class Author(models.Model):
    authorName = models.CharField(max_length=100, null=False, blank=False)
