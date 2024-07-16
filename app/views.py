from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ContactoForm, ProductoForm,CustomCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required,permission_required

def home(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'app/home.html', data)

@login_required
def contacto(request):
    data = {
        'form': ContactoForm()
    }
    
    if request.method == 'POST':
        formulario = ContactoForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto guardado"
        else:
            data["form"] = formulario
    return render(request, 'app/contacto.html', data)

@login_required
def galeria(request):
    return render(request, 'app/galeria.html')


@permission_required('app.add_producto')
def agregar_producto(request):

    data = {
        'form': ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data ["mensaje"] = "guardado exitosamente!!"
        else:
            data["form"] = formulario
    return render(request, 'app/producto/agregar.html', data)

@permission_required('app.view_producto')
def listar_productos(request):
    productos = Producto.objects.all()

    data = {
        'productos': productos
    }
    return render (request, 'app/producto/listar.html', data)

@permission_required('app.change_producto')
def modificar_producto (request, id ):
    producto = get_object_or_404(Producto, id=id)
    data = {
        'form': ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST,instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "modificado correctamente")
            return redirect(to="listar_productos")
        data['form'] = formulario
    return render(request, 'app/producto/modificar.html', data)

@permission_required('app.delete_producto')
def eliminar_producto (request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect(to="listar_productos")


def registro (request):
    data = {
        "form": CustomCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username= formulario.cleaned_data["username"], password = formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "te has registrado correctamente")
            return redirect(to="home")
        data['form'] = formulario
    return render(request,'registration/registro.html', data)




# views.py
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

class CustomLoginView(LoginView):
    def form_valid(self, form):
        user = form.get_user()

        # Verificar si la cuenta está bloqueada
        if user.login_attempts >= 3:
            # Redirigir a la vista de bloqueo
            return HttpResponseRedirect(reverse('bloqueo_view'))

        # Restablecer el contador de intentos fallidos si el inicio de sesión es exitoso
        user.login_attempts = 0
        user.save()

        # Resto del código para el inicio de sesión exitoso
        response = super().form_valid(form)
        return response

    def form_invalid(self, form):
        user = form.get_user()

        # Incrementar el contador de intentos fallidos
        user.login_attempts += 1
        user.save()

        # Bloquear la cuenta después de 3 intentos fallidos
        if user.login_attempts >= 3:
            messages.error(self.request, "Cuenta bloqueada. Por favor, restablece tu contraseña.")
            return HttpResponseRedirect(reverse('password_reset'))

        # Resto del código para el inicio de sesión fallido
        response = super().form_invalid(form)
        return response

# Create your views here.
