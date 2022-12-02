from django.db import models
from datetime import datetime

class Group(models.Model):
    scientific_name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

