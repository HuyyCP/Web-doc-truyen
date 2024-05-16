from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import Chapter

class AddChapterForm(forms.ModelForm):

    class Meta:
        model = Chapter
        fields = ['title']

    def __init__(self, *args, **kwargs):    
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control mb-4'
