from django.shortcuts import render, redirect
from django.views import View
from web.forms import *
from .models import *

# Create your views here.
class AlumnoView(View):
    
    def get(self,request):
        listaAlumnos = TblAlumno.objects.all()
        formAlumno = AlumnoForm()
        context = {
            'alumnos' : listaAlumnos,
            'formAlumno': formAlumno
        }
        return render(request,'index.html',context)

    def post(self, request):
        formAlumno = AlumnoForm(request.POST)
        if formAlumno.is_valid():
            formAlumno.save()
            return redirect('/')
        return render(request, 'index.html')
    
class BorrarView(View):
    def post(self, request, alumno_id):
        # Eliminar el alumno
        alumno = TblAlumno.objects.get(pk=alumno_id)
        alumno.delete()
        return redirect('web:index')

class ProfesorView(View):
    def get(self, request):
        listaProfesores = TblProfesor.objects.all()
        formProfesor = ProfesorForm()
        context = {
            'profesores': listaProfesores,
            'formProfesor': formProfesor
        }
        return render(request, 'profesor.html', context)
    
    def post(self, request):
        formProfesor = ProfesorForm(request.POST)
        if formProfesor.is_valid():
            formProfesor.save()
            return redirect('/profesor')
        return render(request, 'profesor.html')

class ProfesorDeleteView(View):
    def post(self, request, profesor_id):
        profesor = TblProfesor.objects.get(pk=profesor_id)
        profesor.delete()
        return redirect('web:profesor')
        
