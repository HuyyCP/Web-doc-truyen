from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import Manga, Genre

class UploadMangaForm(forms.ModelForm):
    avatarInput = forms.ImageField(label='Cover')

    class Meta:
        model = Manga
        fields = ['title', 'author', 'genres', 'description']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.order_fields(['title', 'avatarInput', 'author', 'genres', 'description'])
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control mb-4'

