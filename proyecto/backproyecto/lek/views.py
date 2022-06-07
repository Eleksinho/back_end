from django.shortcuts import render

# Create your views here.

def menu (request):
    return render (request, 'lek/menu.html')

def contactos (request):
    return render (request, 'lek/contactos.html')
    
def componentes (request):
    contexto = {"nombreC" :"Audifonos","nombreC1":"Hyperx Kraken" , "nombreC2":"Logitech G733", "nombreC3": "Hyperx Cloud Alpha","nombreC4" :"Hyperx Stinger Wireless","nombreC5": "Onikuma Rosado",
                  "fotocomponente1" : "/static/lek/img/componentes/audifono1.png","fotocomponente2" : "/static/lek/img/componentes/audifono2.jpg" , "fotocomponente3" : "/static/lek/img/componentes/audifono3.jpg",
                  "fotocomponente4" : "/static/lek/img/componentes/audifono4.jpg", "fotocomponente5" : "/static/lek/img/componentes/audifono5.jpg"}
    return render (request, 'lek/componentes.html',contexto )

def nosotros (request):
    return render (request, 'lek/nosotros.html')

def registro (request):
    return render (request, 'lek/registro.html')

def login (request):
    return render (request, 'lek/login.html')

def carrito (request):
    return render (request, 'lek/carrito.html')

