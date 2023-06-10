from django.contrib.auth.models import User
from django.db import models

class Item(models.Model):

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'items'

    name = models.CharField(max_length= 255)
    links = models.TextField(blank= True, null =True)

    def __str__(self):
        return self.name