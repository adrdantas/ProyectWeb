from django.shortcuts import render, HttpResponse

def home(request):

    return render(request, "ProyectWebApp/templates/ProyectWebApp/home.html")

def tienda(request):

    return render(request, "ProyectWebApp/templates/ProyectWebApp/tienda.html")

