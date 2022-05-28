from django.urls import URLPattern, path
from .views import menu

urlpatterns = [
    path('',menu,name='menu'),
]