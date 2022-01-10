from django import forms
from django.db.models import fields
from cita.models import Cita


class CitaForm(forms.ModelForm):
    
    class Meta:
        model = Cita
        fields = ['task', 'date', 'status']
        labels = {
            'task': 'Tarea',
            'date': 'Fecha',
            'status': 'Estado',
        }

        widgets = {
            'task': forms.Textarea(attrs={'class': 'form-control'}),
            'email': forms.DateInput(attrs={'class': 'form-control'}),
            'password': forms.Select(choices=Cita.OPCIONES_STATUS, attrs={'class': 'form-control'}),
        }
        



