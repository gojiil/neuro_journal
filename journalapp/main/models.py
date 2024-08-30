from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class TextModel(models.Model):
    """
        Abstract model for text data
    """
    
    class Meta:
        abstract = True

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    last_updated = models.DateTimeField(auto_now=True)

class Tag(models.Model):
    """
        Abstract model for tag data
    """

    class Meta:
        abstract = True

    tagname = models.CharField(max_length=20)
    entryid = models.PositiveBigIntegerField(null=True)
