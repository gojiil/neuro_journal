import logging

from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .forms import NoteForm, EditNoteForm
from .models import Note, NoteTag

logger = logging.getLogger(__name__)

# Create your views here.

def notes_page(request):
    if request.user.id != None:
        queryset_notes = Note.objects.all().filter(user=request.user)
        queryset_tags = NoteTag.objects.all()
        context = {'notes': queryset_notes, 'tags': queryset_tags}
        return render(request, 'notes.html', context)
    else:
        return render(request, 'notes.html')

def edit_note(request, note_id=None):
    message = 'Error'
    if request.method == 'POST':
        if note_id:
            note = Note.objects.get(pk=note_id)
            form = EditNoteForm(request.POST, instance=note)
            if form.is_valid():
                text = form.cleaned_data['text']
                note = Note(pk=note_id, user=request.user, text=text)
                note.save()
                message = 'Note saved'
        else:
            form = NoteForm(request.POST)
            if form.is_valid():
                text = form.cleaned_data['text']
                note = Note(user=request.user, text=text)
                note.save()
                message = 'Note saved'
        queryset = Note.objects.all().filter(user=request.user)
        context = {'notes': queryset, 'message': message }
        return render(request, 'notes.html', context)
    else:
        if note_id:
            note = Note.objects.get(pk=note_id)
            form = EditNoteForm(instance=note)
            message = 'Edit form'
        else:
            form = NoteForm()
            message = 'Fill out form'
    return render(request, 'note.html', { 'form': form, 'message': message })