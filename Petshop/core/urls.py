from django.urls import path
from .views import index, productoRegistro


urlpatterns = [
    path('', index, name="index"),
    path('registroProducto/<action>/<id>', productoRegistro, name="registroProducto"),
]