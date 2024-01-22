from django.db import models

# Create your models here.

class Events(models.Model):
    title = models.CharField(max_length = 100)
    artist_name = models.CharField(max_length = 50)
    date = models.DateField()
    desc = models.TextField(max_length = 200)
    
    def __str__(self):
        return self.title