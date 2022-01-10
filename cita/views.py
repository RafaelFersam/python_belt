from django.shortcuts import render, HttpResponse, redirect
from cita.forms import CitaForm
from django.contrib import messages
from cita.models import Cita

from cita.models import Cita

def index(request):
    context = {
        'citas': Cita.objects.all()
    }
    return render(request, 'index.html', context)


def add(request):
    
    if request.method == 'POST':
        
        form = CitaForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            messages.success(request, "Tarea creada correctamente")
            return redirect('/cita')
        else:
            messages.error(request, "Tarea procesada con errroes.")
            return render(request, 'add.html', {'form':form})
    else:
        context = {
            'form': CitaForm()
        }
        return render(request, 'add.html', context)

def edit(request,id):
    cita = Cita.objects.get(id=id)
    if request.method == 'POST':
        form = CitaForm(request.POST, instance=cita)
        if form.is_valid():
            form.save(commit=False)
            messages.success(request, "Tarea editada correctamente")
            return redirect('/cita')
    else:
        form = CitaForm(instance=cita)
        return render(request, 'edit.html', {'fomr': form, 'cita': cita})
        
def delete(request,id):
    pass