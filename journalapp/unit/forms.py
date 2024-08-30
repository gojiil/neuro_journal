from typing import Any, Mapping
from django import forms
from django.forms.renderers import BaseRenderer
from django.forms.utils import ErrorList
from .models import Unit

class URLForm(forms.Form):

    url = forms.CharField(label='Url', widget=forms.widgets.TextInput)

class UnitForm(forms.Form):
    
    url = forms.CharField(label='Url', widget=forms.widgets.TextInput)
    unit = forms.CharField(label='Текст', widget=forms.widgets.Textarea, required=False)
    text = forms.CharField(label='Заметка', widget=forms.widgets.Textarea, required=False)
        

class EditUnitForm(forms.ModelForm):

    class Meta:
        model = Unit
        fields = ('url', 'unit', 'text',)
        labels = {
            'url': 'Url',
            'unit': 'Текст',
            'text': 'Заметка'
        }