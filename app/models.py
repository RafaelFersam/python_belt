from django.db import models

# Create your models here.
class User(models.Model):
    
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['name']
        
    def __str__(self):
        return f"{self.name} ({self.role})"