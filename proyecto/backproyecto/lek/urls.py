from django.urls import path
from .views import menu, componentes, contactos

urlpatterns = [
    path('',menu,name='menu'),
    path('componentes',componentes,name='componentes'),
    path('contactos/',contactos,name='contactos'),
    
]
