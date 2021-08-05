from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def title(request):
    return render(request, 'core/title.html')

def about(request):
    about = '<p> Hi, i´m Alan and i like programing and bla bla bla</p>'
    return HttpResponse(about)

def port(request):
    portafolio = '<p> The languages than i´m learning: Python, Java, Lisp and Peeeeeerl </p>'
    return HttpResponse(portafolio)

def cont(request):
    contact = '<p> Tel: 2281742 </p>'
    return HttpResponse(contact)

# Request => Solicitud
# Response => Respuesta