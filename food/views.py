from django.shortcuts import render, get_object_or_404, redirect
from .models import Food
from .forms import FoodForm
# Create your views here.

def food_list(request):
    qs = Food.objects.all()
    return render(request, 'food/food_list.html',{
        'posts':qs,
    })

def food_new(request):
    if request.method =="POST":
        form = FoodForm(request.POST, request.FILES)
        if(form.is_valid()):
            food = form.save()
            return redirect('/food/')
    else:
        form = FoodForm()

    return render(request, 'food/food_new.html', {'form':form})


def food_detail(request, id):
    qs = get_object_or_404(Food, id=id)
    return render(request, 'food/food_detail.html',{
        'post':qs,
    })
