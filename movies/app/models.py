from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)

    def __str__(self):
        return f'Name: {self.name} - Description: {self.description}'
    
