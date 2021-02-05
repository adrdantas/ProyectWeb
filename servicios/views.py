from django.shortcuts import render
from servicios.models import Servicio

def servicios(request):

    servicios = Servicio.objects.all()
    return render(request, "servicios/templates/servicios/servicios.html", {"servicios": servicios})
