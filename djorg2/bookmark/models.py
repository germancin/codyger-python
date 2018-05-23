from django.db import models
from uuid import uuid4

# Create your models here.

class Bookmarks(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    url = models.URLField('URL', unique=True, default='')
    name = models.CharField(max_length=200, default='')
    notes = models.TextField(blank=True, default='')