from django.db import models

# Create your models here.

class Bookmarks(models.Model):

    notes = models.TextField(blank=True)