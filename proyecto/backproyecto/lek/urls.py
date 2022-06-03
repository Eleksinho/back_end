from django.urls import path
from .views import componentes, menu,contactos

urlpatterns = [
    path('menu',menu,name='menu'),
    path('contactos/',contactos,name='contactos'),
    path('',componentes,name='componente'),
]
