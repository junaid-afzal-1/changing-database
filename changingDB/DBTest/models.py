from django.db import models
from datetime import datetime

class Temp(models.Model):

    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField(default=0)
    time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = "Temp"
        verbose_name_plural = "Temps"

    def __str__(self):
        return self.name

