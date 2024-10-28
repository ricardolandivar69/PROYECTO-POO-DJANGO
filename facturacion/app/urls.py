from django.urls import path
from .views import insertar_datos_iniciales, ver_datos

urlpatterns = [
    path('insertar_datos/', insertar_datos_iniciales, name='insertar_datos'),
    path('ver_datos/', ver_datos, name='ver_datos'),  
]
