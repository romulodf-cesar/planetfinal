from django.urls import path
from galeria.views import index
from galeria.views import imagem

urlpatterns = [
    path('', index,name='index'),
    path('imagem/<int:foto_id>',imagem,name='imagem'),
    
]

