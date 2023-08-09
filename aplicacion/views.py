from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'aplicacion/base.html')

#-----------------------articulos-----------------------------------------------
def articulos(request):
    ctx = {"articulos": Articulo.objects.all()}
    return render(request, 'aplicacion/articulos.html', ctx)

def articulosForm(request):
    if request.method == "POST":
        miForm = ArticuloForm(request.POST)
        print(miForm)
        if miForm.is_valid:
            informacion = miForm.cleaned_data
            articulo = Articulo(nombre=informacion['nombre'], marca=informacion['marca'], modelo=informacion['modelo'], origen=informacion['origen'])
            articulo.save()
            return render(request, 'aplicacion/base.html')
    else:
        miForm = ArticuloForm()
        
    return render(request, 'aplicacion/articulosForm.html', {"form":miForm})

#-----------------------cursos-----------------------------------------------
def cursos(request):
    ctx= {"cursos": Curso.objects.all()}
    return render(request, 'aplicacion/cursos.html', ctx)

def cursosForm(request):
    if request.method == "POST":
        miForm = CursoForm(request.POST)
        print(miForm)
        if miForm.is_valid:
            informacion = miForm.cleaned_data
            curso = Curso(nombre=informacion['nombre'], comision=informacion['comision'], nombreAlumno=informacion['nombreAlumno'])
            curso.save()
            return render(request, 'aplicacion/base.html')
    else:
        miForm = CursoForm()
        
    return render(request, 'aplicacion/cursosForm.html', {"form":miForm})

#-----------------------ofertas-----------------------------------------------
def ofertas(request):
    ctx= {"ofertas": Oferta.objects.all()}
    return render(request, 'aplicacion/ofertas.html', ctx)

def ofertasForm(request):
    if request.method == "POST":
        miForm = OfertaForm(request.POST)
        print(miForm)
        if miForm.is_valid:
            informacion = miForm.cleaned_data
            oferta = Oferta(nombre=informacion['nombre'], marca=informacion['marca'], modelo=informacion['modelo'], descuentoEspecial=informacion['descuentoEspecial'])
            oferta.save()
            return render(request, 'aplicacion/base.html')
    else:
        miForm = OfertaForm()
        
    return render(request, 'aplicacion/ofertasForm.html', {"form":miForm})

#-----------------------partner-----------------------------------------------
def partners(request):
    ctx = {"partners": Partner.objects.all()}
    return render(request, 'aplicacion/partners.html',ctx)

def partnersForm(request):
    if request.method == "POST":
        miForm = PartnerForm(request.POST)
        print(miForm)
        if miForm.is_valid:
            informacion = miForm.cleaned_data
            partner = Partner(nombre=informacion['nombre'], antiguedad=informacion['antiguedad'])
            partner.save()
            return render(request, 'aplicacion/base.html')
    else:
        miForm = PartnerForm()
        
    return render(request, 'aplicacion/partnersForm.html', {"form":miForm})

#---------------------------------funcion buscar--------------------------

def buscarComision(request):
    return render(request, "aplicacion/buscarComision.html")

def buscar2(request):
    if request.GET['comision']:
        comision = request.GET['comision']
        cursos = Curso.objects.filter(comision__icontains=comision)
        return render(request, 
                      "aplicacion/resultadosComision.html",
                      {"comision": comision, "cursos": cursos})
    return HttpResponse("No se ingresaron datos para realizar busqueda")