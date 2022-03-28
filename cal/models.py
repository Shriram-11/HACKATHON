from django.db import models
# Create your models here.

class Cal(models.Model):
    sr = models.IntegerField()
    event = models.CharField(max_length=1024)
    date = models.DateField()
    note = models.CharField(max_length=256)
    img_url = models.CharField(max_length=2048)

