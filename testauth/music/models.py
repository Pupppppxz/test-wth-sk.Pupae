from datetime import date

from django.db import models


from django.db import models
from django.conf import settings


# Create your models here.
class Songs(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, null=False)
    artist = models.CharField(max_length=255, null=False)
    song = models.FileField(upload_to='' , null=True)
    album = models.ImageField(upload_to ='album/',null=True)
    release = models.DateField(default=date.today().strftime("%d-%m-%Y"))
    image = models.ImageField(upload_to='cover/', null=True)
    like = models.IntegerField(default=0)
    view = models.IntegerField(default=0)
    
    def __str__(self):
        return "{}".format(self.title)
