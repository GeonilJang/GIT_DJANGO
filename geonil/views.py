from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from .models import Show
from .forms import ShowForm

# Create your views here.
def show_geonil(request):
    if(request.method == 'POST'):
        form = ShowForm(request.POST, request.FILES)
        if(form.is_valid()): #토큰 여부 체크
            print(form.cleaned_data)
            form = form.save()
            return redirect('/geonil/')
    else:
        form = ShowForm()
    return render(request, 'geonil/show_geonil.html')
