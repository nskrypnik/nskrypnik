from django.db import models
from datetime import datetime

class Status(models.Model):
    text = models.CharField(max_length=256)
    date_added = models.DateTimeField(default=datetime.now())

