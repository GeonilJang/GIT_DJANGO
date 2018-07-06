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


def food_edit(request, id):
    post = get_object_or_404(Food, id=id)
    print(post)
    if (request.method == 'POST'):
        form = FoodForm(request.POST, request.FILES, instance=post)
        if(form.is_valid()): #토큰을 가지고 들어왔다면 !
            post = form.save(commit=False) #아래에서 커빗 하고싶어서 !!
            post.ip = request.META['REMOTE_ADDR'] #화면을 통해 입력 받지 않는 데이터를 데이버페이스에 저장하고 싶을때 쓰는방법
            post.save()
            return redirect('/food/')
    else:
        form = FoodForm(instance=post)
    return render(request, 'food/food_new.html',{
        'form':form,
    })
