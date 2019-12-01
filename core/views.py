from django.shortcuts import render

from catalog.models import *

# Create your views here.
def index(request):
    context = {}
    context["categorias"] = ModelCategoria.objects.all()
    return render(request,'index.html',context)

