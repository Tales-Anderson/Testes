from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from .form import *

# Create your views here.

def home(request):
    var = {}
    var ['apartamentos'] = Apartamento.objects.all()
    return render(request, 'inicio.html', var)


def homeFunc(request):
    var = {}
    var ['apartamentos'] = Apartamento.objects.all()
    return render(request, 'iniciofunc.html', var)



def add_apartamento(request):
    form = ApartamentoForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('url_HomeFunc')

    return render(request, 'form.html', {'form': form})


def update(request, pk):
    apartamento = Apartamento.objects.get(pk=pk)
    form = ApartamentoForm(request.POST or None, instance=apartamento)

    if form.is_valid():
        form.save()
        return redirect('url_HomeFunc')

    return render(request, 'form.html', {'form': form})


def delete(request, pk):
    apartamento = Apartamento.objects.get(pk=pk)
    apartamento.delete()

    return redirect('url_HomeFunc')
