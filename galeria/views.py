from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from galeria.models import Fotografia
def index(request):
    #fotografia = Fotografia.objects.all()
    #fotografia = Fotografia.objects.filter(publicada=True)  
    fotografia = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)
    return render(request, 'galeria/index.html',{"cards":fotografia})

def imagem(request,foto_id):
    fotografia = get_object_or_404(Fotografia,pk=foto_id)
    return render(request, 'galeria/imagem.html',{"fotografia":fotografia})

#def buscar(request):
#    return render(request,"galeria/buscar.html")

def buscar(request):
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)

    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar'] #galaxia
        if nome_a_buscar: 
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)
    return render (request,"galeria/buscar.html",{"cards":fotografias})

