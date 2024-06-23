from django.shortcuts import render



def index(request):
    dados = {
        1: {"nome": "Nebulosa de Carina", "legenda": "webtelescope.org / Nasa / James Webb"},
        2: {"nome": "Estrela NGC 3324", "legenda": "nasa.org / Nasa / Hubble"},
    }
    
    return render(request, 'galeria/index.html', {"cards": dados})


def imagem(request):
    return render(request, 'galeria/imagem.html')
