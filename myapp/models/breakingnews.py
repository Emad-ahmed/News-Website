from django.db import models


class BreakNews(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    images = models.ImageField(upload_to='images/')
