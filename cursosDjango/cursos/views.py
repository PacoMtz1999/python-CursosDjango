from django.shortcuts import render
from .forms import MensajeUsuarioForm
from .forms import registroCurso
from .models import Cursos
from django.shortcuts import get_object_or_404

# Create your views here.

def principal(request):
    return render(request,"cursos/principal.html")

def registrar(request):
    if request.method == 'POST':
        form = MensajeUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"cursos/contacto.html")
    form = MensajeUsuarioForm()
    return render(request,"cursos/contacto.html",{'form':form})

def contacto(request):
    return render(request,"cursos/contacto.html")

def consultaCurso(request):
    cursos=Cursos.objects.all()
    return render(request,"cursos/consultaCurso.html", {'cursos':cursos})

""" def formRegistroCurso(request):
    if request.method == 'POST':
        form = registroCurso(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"cursos/registraCurso.html")
    form = registroCurso()
    return render(request,"cursos/registraCurso.html",{'form':form}) """

def formRegistroCurso(request):
    if request.method == 'POST':
        form = registroCurso(request.POST)
        if form.is_valid():
            form.save()
            cursos=Cursos.objects.all()
            return render(request,"cursos/consultaCurso.html",{'cursos':cursos})
    form = registroCurso()
    return render(request,"cursos/registraCurso.html",{'form':form})

def registraCurso(request):
    return render (request,"cursos/registraCurso.html")

def eliminarCurso(request, id, confirmacion='cursos/confirmarEliminacion.html'):
    curso = get_object_or_404(Cursos, id=id)
    if request.method=='POST':
        curso.delete()
        cursos=Cursos.objects.all()
        return render(request,"cursos/consultaCurso.html",{'cursos':cursos})
    return render(request, confirmacion, {'object':curso})

def consultaCursoIndividual(request, id):
    curso=Cursos.objects.get(id=id)
    return render(request,"cursos/formEditarCurso.html",{'curso':curso})

def editaCurso(request, id):
    curso = get_object_or_404(Cursos, id=id)
    form = registroCurso(request.POST, instance=curso)
    if form.is_valid():
        form.save()
        cursos=Cursos.objects.all()
        return render(request,"cursos/consultaCurso.html",{'cursos':cursos})
    return render(request,"cursos/formEditarCurso.html",{'curso':curso})