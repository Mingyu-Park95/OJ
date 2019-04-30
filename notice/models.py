from django.db import models

# Create your models here.


class Notice(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    date = models.DateTimeField(auto_now=True)