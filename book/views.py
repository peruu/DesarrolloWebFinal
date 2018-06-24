from django.shortcuts import render

# Create your views here.
def index(request):
    template_name = "base.html"
    return render(request,template_name)
def prueba(request):
    template_name = "prueba.html"
    return render(request,template_name)
