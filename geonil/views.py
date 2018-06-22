from django.shortcuts import render
from django.http import HttpResponse , JsonResponse


# Create your views here.
def show_geonil(request):
    return render(request, 'geonil/show_geonil.html')
