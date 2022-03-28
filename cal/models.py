from django.db import models
# Create your models here.

class Cal(models.Model):
    sr = models.IntegerField()
    Img_url = models.CharField(max_length=2048)
    uni = models.CharField(max_length=256)
    state = models.CharField(max_length=256) 
    title = models.CharField(max_length=1024)
    date = models.DateField()
    link = models.CharField(max_length=2048)
