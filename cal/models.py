from django.db import models
# Create your models here.

class Cal(models.Model):
    Sr = models.IntegerField()
    Event = models.CharField(max_length=1024)
    Date = models.DateField()
    Note = models.CharField(max_length=256)
    Img_url = models.CharField(max_length=2048)

