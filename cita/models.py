from django.db import models
import re

# Create your models here.


class Cita(models.Model):
    
    PENDING = 'P'
    DONE = 'D'
    MISSED = 'M'
    
    OPCIONES_STATUS = [
        (PENDING, 'Pending'),
        (DONE, 'Done'),
        (MISSED, 'Missed')
    ]
    task = models.TextField()
    date = models.DateField()
    status = models.CharField(max_length=1, choices=OPCIONES_STATUS, default=PENDING)
    


    class Meta:
        verbose_name = 'Cita'
        verbose_name_plural = 'Citas'

def __str__(self):
    return f"{self.task} ({self.status})"
