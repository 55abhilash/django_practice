from __future__ import unicode_literals

from django.db import models
import datetime
# Create your models here.

class posts(models.Model):
    author = models.CharField(max_length = 30)
    title = models.CharField(max_length = 100)
    bodytext = models.TextField()
    timestamp = models.DateTimeField()

class insert():
    x = posts(author="abc", title="tit", bodytext="alsjkdfl", timestamp=datetime.date(1995, 2, 2))
    x.save()

