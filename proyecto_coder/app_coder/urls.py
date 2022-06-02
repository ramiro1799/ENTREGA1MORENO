from django import views
from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio),
    path("cursos" , views.cursos),
    path("alumnos", views.alumnos),
    path("contacto", views.contacto),
    path("alta_curso/<nombre>" , views.alta_curso)
    
]
