from django.shortcuts import render

# Create your views here.

def menu (request):
    return render (request, 'lek/menu.html')

def contactos (request):
    return render (request, 'lek/contactos.html')
    
def componentes (request):
    contexto = {"nombreC" :"Audifonos","nombreC1":"Hyperx Kraken" , "nombreC2":"Logitech G733", "nombreC3": "Hyperx Cloud Alpha","nombreC4" :"Hyperx Stinger Wireless","nombreC5": "Onikuma Rosado",
                  "fotocomponente1" : "/static/lek/img/componentes/audifono1.png","fotocomponente2" : "/static/lek/img/componentes/audifono2.png" , "fotocomponente3" : "/static/lek/img/componentes/audifono3.png",
                  "fotocomponente4" : "/static/lek/img/componentes/audifono4.png", "fotocomponente5" : "/static/lek/img/componentes/audifono5.png"}
    return render (request, 'lek/componentes.html',contexto )

