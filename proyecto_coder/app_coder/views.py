from django.http import HttpResponse
from django.shortcuts import render
from app_coder.models import Curso
from django.template import loader
# Create your views here.

def inicio(request):
    return render(request , "plantillas.html")

def cursos(request):
    cursos = Curso.objects.all()
    dicc = {"cursos" : cursos}
    plantilla = loader.get_template("cursos.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)

def alta_curso(request, nombre):
    curso = Curso(nombre= nombre, camada=287318)
    curso.save()
    texto = f"Se guardo en la BD el Curso: {curso.nombre} Camda: {curso.camada}"
    return HttpResponse(texto)

def alumnos(request):

    return render(request , "alumnos.html")

def contacto(request):
    
    return render(request , "contacto.html")

        