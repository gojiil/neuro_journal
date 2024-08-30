from django.db import models
from main.models import TextModel, Tag

# Create your models here.

class Unit(TextModel):

    url = models.CharField(max_length=100)
    unit = models.TextField()

    def __str__(self) -> str:
        return super().__str__()
    
class UnitTag(Tag):

    def __str__(self) -> str:
        return super().__str__()
