from django.shortcuts import render
from django.http import HttpResponse
from galeria.models import Fotografia
def index(request):
    fotografia = Fotografia.objects.all()   
    return render(request, 'galeria/index.html',{"cards":fotografia})

def imagem(request):
    return render(request, 'galeria/imagem.html')

