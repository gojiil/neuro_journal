from django.db import models
from main.models import TextModel, Tag

# Create your models here.

class Project(TextModel):

    def __str__(self) -> str:
        return super().__str__()
    
class ProjectTag(Tag):

    def __str__(self) -> str:
        return super().__str__()
