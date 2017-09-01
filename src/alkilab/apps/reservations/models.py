from django.db import models

class Room(models.Model):
    """Model definition for Room."""
    name = models.CharField(max_length=100)
