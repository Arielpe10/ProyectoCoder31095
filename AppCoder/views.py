from django.shortcuts import render
from AppCoder.models import Curso
# Create your views here.

def curso(request):
    curso1 = Curso(nombre = "Python", camada = 31095)
    curso1.save()

    return render(request, 'curso.html')