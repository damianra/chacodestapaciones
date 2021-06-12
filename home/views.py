from django.shortcuts import render
from home.models import Publicaciones, Contacto, RedesSociales
from home.form import ContactoForm
from datetime import datetime
from django.http import HttpResponse, JsonResponse

# Create your views here.
def index(request):
    redes = RedesSociales.objects.all()
    form = ContactoForm()

    return render(request, 'home/index.html', {'redes': redes, 'form': form})


def servicios(request):
    serv = Publicaciones.objects.filter(titulo='Servicios').first()
    redes = RedesSociales.objects.all()
    contenido = { 'servicios': serv, 'redes': redes }
    return render(request, 'home/servicios.html', contenido)

def quienesSomos(request):
    quien = Publicaciones.objects.filter(titulo='Quienes Somos').first()
    redes = RedesSociales.objects.all()
    contenido = { 'servicios': quien, 'redes': redes }
    return render(request, 'home/servicios.html', contenido)

def contacto(request):
    if request.method == 'POST':
                
        if request.is_ajax:
            form = ContactoForm(request.POST)
            if form.is_valid():
                nombre = form.cleaned_data['nombre']
                email = form.cleaned_data['email']
                telefono = form.cleaned_data['telefono']
                mensaje = form.cleaned_data['mensaje']
                fecha = datetime.now()
                nuevo_mensaje = Contacto(nombre=nombre, email=email, telefono=telefono, mensaje=mensaje, fecha=fecha)
                nuevo_mensaje.save()

                data_json = JsonResponse({'response': 'success'})
                mimetype = "application/json"
                return HttpResponse(data_json, mimetype)
            else:
                data_json = JsonResponse({'response': 'fail'})
                mimetype = "application/json"
                return HttpResponse(data_json, mimetype)
    else:
        redes = RedesSociales.objects.all()
        form = ContactoForm()
    return render(request, 'home/contacto.html', {'form': form, 'redes': redes})

