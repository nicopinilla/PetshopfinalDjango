from django.shortcuts import render
from .models import Producto
from .forms import ProductoForm


# Create your views here.
from django.shortcuts import render
""" from .models import UsuarioDonador
from .forms import UsuarioDonadorForm,DonacionForm """

def index(request):
    return render(request, "core/index.html")

def productoRegistro(request, action, id):
    data = {"mesg": "", "form": ProductoForm, "action": action, "id": id}

    if action == 'ins':
        if request.method == "POST":
            form = ProductoForm(request.POST, request.FILES)
            if form.is_valid:
                try:
                    form.save()
                    data["mesg"] = "¡El producto fue creado correctamente!"
                except:
                    data["mesg"] = "¡El producto ya esta registrado!"
    return render(request, "core/registroProducto.html", data)