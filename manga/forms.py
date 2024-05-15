from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import Manga, Genre

class UploadMangaForm(forms.ModelForm):
    avatarInput = forms.ImageField(label='Cover')
    # options = forms.MultipleChoiceField(
    #     widget=forms.CheckboxSelectMultiple,
    #     choices=[('option1', 'Option 1'), ('option2', 'Option 2'), ('option3', 'Option 3')]
    # )

    class Meta:
        model = Manga
        fields = ['title', 'author', 'genres', 'description']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.order_fields(['title', 'avatarInput', 'author', 'genres', 'description'])
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control mb-4'
        # self.fields['genres'].widget = forms.CheckboxSelectMultiple(attrs={'class': 'form-control mb-4'})


class EditMangaForm(forms.ModelForm):
    avatarInput = forms.ImageField(label='Cover', required=False)

    class Meta:
        model = Manga
        fields = ['title', 'author', 'avatarLink', 'genres', 'description']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.order_fields(['title', 'avatarInput', 'author', 'avatarLink', 'genres', 'description'])
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control mb-4'
        # self.fields['author'].widget.attrs['required'] = False
        self.fields['author'].widget.attrs['disabled'] = True
        self.fields['author'].required = False

