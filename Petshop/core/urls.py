from django.urls import path
from .views import contacto, index, editor_producto,lista_producto,producto_ficha,sobrenosotros,login, carrito 


urlpatterns = [
    path('', index, name="index"),
    path('editorProducto/<action>/<id>', editor_producto, name="editorProducto"),
    path('producto_tienda/', lista_producto, name="tiendaProducto"),
    path('producto_ficha/<id>', producto_ficha, name="producto_ficha"),
    path('sobrenosotros/', sobrenosotros, name="sobrenosotros"),
    path('contacto/', contacto, name="contacto"),
    path('login/', login, name="login" ),
    path('carrito/', carrito, name="carrito")

]