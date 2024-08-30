from django.db import models
from main.models import TextModel, Tag

# Create your models here.

class Note(TextModel):

    def __str__(self) -> str:
        return super().__str__()
    
class NoteTag(Tag):

    def __str__(self) -> str:
        return super().__str__()
