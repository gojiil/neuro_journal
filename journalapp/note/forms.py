from typing import Any
from django import forms
from .models import Note

class NoteForm(forms.Form):

    text = forms.CharField(label='Заметка', widget=forms.widgets.Textarea)

class EditNoteForm(forms.ModelForm):
    
    class Meta:
        model = Note
        fields = ('text',)