from django.urls import path
from .views import menu,contactos

urlpatterns = [
    path('',menu,name='menu'),
    path('contactos/',contactos,name='contactos'),
]
