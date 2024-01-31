from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from .forms import Register ,LoginForm, Pedido
from .models import Usuario, Pedidos
from django.conf import settings



def inicio(request):
    
    context={}
    return render(request, "inicio.html", context)


# Esta funcion sirve para registrar un usuario en la base de datos
def registro(request):
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            # Obtén los datos del formulario
            RazonS = form.cleaned_data['RazonS']
            DireccionF = form.cleaned_data['DireccionF']
            CodigoP = form.cleaned_data['CodigoP']
            RFC = form.cleaned_data['RFC']
            DireccionE = form.cleaned_data['DireccionE']
            email = form.cleaned_data['Email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Usa make_password para hashear la contraseña antes de almacenarla
            hashed_password = make_password(password)

            # Crea una instancia de Usuario y guárdala en la base de datos
            usuario = Usuario(RazonS=RazonS, DireccionF=DireccionF, CodigoP=CodigoP, RFC=RFC, DireccionE=DireccionE, Email=email, username=username, password=hashed_password)
            usuario.save()

            # Redirecciona a una página de éxito o realiza otras acciones necesarias
            return redirect('web:login')  # Cambia 'pagina_de_exito' por la URL a la que quieras redirigir

    else:
        form = Register()
    
    context = {
        'form': form,
    }
    return render(request, "registro.html", context)


#Esta funcion sirve para que el usuario inicie sesion autenticandolo y verificandolo desde la base de datos
def login(request):
    if request.user.is_authenticated:
        return redirect('web:dashboard')
    form = LoginForm(request.POST or None)
    if form.is_valid():
        login = form.cleaned_data['username']
        password = form.cleaned_data['password']
        usuario = authenticate(request, login=login, password=password)
        if usuario is not None:
            auth_login(request, usuario)
            if 'next' in request.GET:
                return redirect(request.GET['next'])
            return redirect("web:dashboard")
        else:
            messages.error(request, """Por favor introduzca un nombre de usuario y contraseña correctos. 
                           Si aún no estás registrado haz clic en el enlace de abajo Regístrate Aquí.""")
            return redirect('web:login')
    context = {
        'form': form,
    }
    return render(request, 'registration/login.html', context)


#Esta funcion sirve para desloguear al usuario de su cuenta y mandarlo al login
def logout(request):
    auth_logout(request)

    return redirect('web:login')


#Esta funcion sirve para guardar la orden de trabajo generada por el usuario logueado en el dashboard
def dashboard(request):
    if request.method == 'POST':
        form = Pedido(request.POST)
        if form.is_valid():
            moneda = form.cleaned_data['Moneda']
            solicitante = form.cleaned_data['Solicitante']
            empresa = form.cleaned_data['Empresa']
            direccion = form.cleaned_data['Direccion']
            telefono = form.cleaned_data['Telefono']
            cantidad = form.cleaned_data['Cantidad']
            detalles = form.cleaned_data['Detalles']

            datos = Pedidos(
                Moneda=moneda,
                Solicitante=solicitante,
                Empresa=empresa,
                Direccion=direccion,
                Telefono=telefono,
                Cantidad=cantidad,
                Detalles=detalles
            )
            datos.save()

            return redirect('web:dashboard')
            print("Formulario no válido")
            print(form.errors)  

    else:
        form = Pedido()
        print("Formulario no válido")
        print(form.errors)  
    
    context = {
        'form': form,
    }

    return render(request, "dashboard.html", context)




