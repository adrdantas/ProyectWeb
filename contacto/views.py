from django.shortcuts import render, redirect

from .forms import FormularioContacto

from django.core.mail import EmailMessage


def contacto(request):
    formulario_contacto = FormularioContacto()

    if request.method == "POST":
        formulario_contacto = FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")

            email = EmailMessage("Mensagem do App do Django",
                                 "O usuário com o nome {} com o e-mail lhe escreve o seguinte:\n\n {}".format(nombre, email, contenido),
                                 "", ["adrdantasrodrigues@gmail.com"], reply_to=[email])

            try:
                email.send()
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?novalido")

    return render(request, "contacto/templates/contacto/contacto.html", {'miFormulario': formulario_contacto})

