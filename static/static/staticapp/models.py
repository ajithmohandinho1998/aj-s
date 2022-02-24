from django.db import models

# Create your models here.
class places(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

class team(models.Model):
    tname=models.CharField(max_length=250)
    timg=models.ImageField(upload_to='pics')
    tdesc=models.TextField()



