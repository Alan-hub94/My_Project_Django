from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    title = '<h1> Mi primera vista de Django </h1>'
    content = ''

    for i in range(10):
        content += '<p> Yo soy un parrafo (for) en el ciclo: ' + str(i+1) + '<p>'
    return HttpResponse(title + content)

def home(request):
    title = '<h1> Homework </h1>'
    about = '<p> about </p>'
    portafolio = '<p> portafolio </p>'
    contact = '<p> contacto </p>'
    return HttpResponse(title + about + portafolio + contact)

# Request => Solicitud
# Response => Respuesta