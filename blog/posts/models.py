from django.db import models
from datetime import datetime
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000)
    date  = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return str(self.id)+ self.title
