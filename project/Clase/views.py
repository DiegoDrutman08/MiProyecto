from django.shortcuts import render, redirect
from .models import Curso, Estudiante, Profesor, Comision

def home(request):
    return render(request, "core/base.html")

def agregar_curso(request):
    if request.method == 'POST':
        nombre_curso = request.POST.get('curso')
        Curso.objects.create(nombre=nombre_curso)
        return redirect('core:home')
    else:
        return render(request, 'core/base.html')

def agregar_estudiante(request):
    if request.method == 'POST':
        nombre_estudiante = request.POST.get('estudiante')
        Estudiante.objects.create(nombre=nombre_estudiante)
        return redirect('core:home')
    else:
        return render(request, 'core/base.html')

def agregar_profesor(request):
    if request.method == 'POST':
        nombre_profesor = request.POST.get('profesor')
        edad_profesor = request.POST.get('edad')
        Profesor.objects.create(nombre=nombre_profesor)
        Profesor.objects.create(edad=edad_profesor)
        return redirect('core:home')
    else:
        return render(request, 'core/base.html')

def agregar_comision(request):
    if request.method == 'POST':
        nombre = request.POST.get('comision')
        curso_id = request.POST.get('cursos')
        profesor_id = request.POST.get('profesores')
        estudiantes_ids = request.POST.getlist('estudiantes')

        estudiantes_ids = [int(id) for id in estudiantes_ids]

        comision = Comision.objects.create(
            nombre=nombre,
            curso=Curso.objects.get(id=curso_id),
            profesor=Profesor.objects.get(id=profesor_id)
        )
        comision.estudiante.set(estudiantes_ids)

        return redirect('core:home')
    else:
        cursos = Curso.objects.all()
        profesores = Profesor.objects.all()
        estudiantes = Estudiante.objects.all()

        return render(request, 'core/agregar_comision.html', {'cursos': cursos, 'profesores': profesores, 'estudiantes': estudiantes})




