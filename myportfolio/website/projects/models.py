from django.db import models
from time import time
from turtle import title
from django.urls import reverse
import datetime
# Create your models here.


class Projects(models.Model):
    image = models.ImageField(upload_to='media')
    name = models.CharField(max_length=100, null=False)
    date = models.DateField(default=datetime.date.today())
    responsive = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.name