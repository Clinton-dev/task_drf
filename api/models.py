from ast import mod
from django.db import models

class Task(models.Model):
    text = models.CharField(max_length=200)
    day = models.CharField(max_length=200)
    reminder = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __str__(self) -> str:
        return self.text[0:50]