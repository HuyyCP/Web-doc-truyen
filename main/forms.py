from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from genre.models import Genre

class SearchForm(forms.Form):
    genresIncluded = forms.CharField(widget=forms.HiddenInput(), required=False)    
    genresExcluded = forms.CharField(widget=forms.HiddenInput(), required=False)    
    