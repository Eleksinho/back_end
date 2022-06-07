from django.urls import path
from .views import menu, componentes, contactos, nosotros

urlpatterns = [
    path('',menu,name='menu'),
    path('componentes',componentes,name='componentes'),
    path('contactos/',contactos,name='contactos'),
    path('nosotros/',nosotros,name='nosotros'),
    
]
