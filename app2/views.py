from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index2(request):
    return HttpResponse("<h1> Soy el index de la app2 </h1>")

def saludo(request):
    html="""
    <h1> Soy la página 1 de la app2 </h1>
    <a href="/app2/index2">Volver</a>
    """
    return HttpResponse(html)

def testeo2(request):
    return HttpResponse("<h2> Isaac kept to himself - drawing pictures and playing with his toys as his mom watched Christian broadcasts on the television. </h2>")

def pag2(request):
	html="""
    <h1 style ="color:red"> Soy la página 2 </h1>
    """
	return HttpResponse(html)