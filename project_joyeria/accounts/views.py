from django.shortcuts import render,redirect

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from accounts.forms import *
from django.contrib import messages  # Importa el sistema de mensajes
from .models import Imagen
from django.contrib.auth.decorators import login_required

# Create your views here.
def aboutUs(request):
    return render(request,'accounts/aboutUs.html')
    
def login_usr(request):
    msg_login = ""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)
                return render(request, "AppJoyeria/inicio.html")

        msg_login = "Usuario o contraseña incorrectos"

    form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form": form, "msg_login": msg_login})


def registro(request):
    if request.method == 'POST':
        form = RegistroUsuario(request.POST)
        if form.is_valid():
            form.save()
            # Agregar mensaje de éxito
            messages.success(request, "Te has registrado exitosamente. Ahora puedes iniciar sesión.")
            return redirect('login')  # Redirige a la vista de login
        else:
            # Agregar mensaje de error
            messages.error(request, "Error en los datos ingresados")
    else:
        form = RegistroUsuario()

    return render(request, "accounts/registro.html", {"form": form})
@login_required
def editar_usr(request):
    usuario = request.user

    if request.method == 'POST':

        miFormulario = EditarUsuario(request.POST, request.FILES)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            if informacion["password1"] != informacion["password2"]:
                datos = {
                    'nombre': usuario.first_name,
                    'email': usuario.email
                }
                miFormulario = EditarUsuario(initial=datos)

            else:
                usuario.email = informacion['email']
                if informacion["password1"]:
                    usuario.set_password(informacion["password1"])
                usuario.last_name = informacion['nombre']
                usuario.first_name = informacion['apellido']
                usuario.save()

                # Creamos nueva imagen en la tabla
                try:
                    avatar = Imagen.objects.get(user=usuario)
                except Imagen.DoesNotExist:
                    avatar = Imagen(user=usuario, imagen=informacion["imagen"])
                    avatar.save()
                else:
                    avatar.imagen = informacion["imagen"]
                    avatar.save()

                return redirect('inicio')

    else:
        datos = {
            'nombre': usuario.first_name,
            'email': usuario.email
        }
        miFormulario = EditarUsuario(initial=datos)

    return render(request, "accounts/edit.html", {"mi_form": miFormulario, "usuario": usuario})

